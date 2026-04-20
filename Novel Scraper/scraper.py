"""
╔══════════════════════════════════════════════════════════╗
║  🍤 甜蝦小說爬蟲 - 小說狂人 (czbooks.net)               ║
║  自動抓取整本小說，輸出為純文字檔。                      ║
║  使用方式：修改下方「設定區」的網址後，直接執行即可。    ║
╚══════════════════════════════════════════════════════════╝
"""

import cloudscraper
from bs4 import BeautifulSoup
import time
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ============================================================
#  📌 設定區 - 只需要改這裡就好
# ============================================================

# 小說的「目錄頁」網址（不是章節頁喔！）
# 例如：https://czbooks.net/n/skdocomojaf
NOVEL_URL = "https://czbooks.net/n/skdocomojaf"

# 輸出檔名（會存在與此腳本同一目錄下）
OUTPUT_FILE = "novel_output.txt"

# 每頁之間的等待秒數（避免被網站封鎖，建議 2~5 秒）
DELAY_SECONDS = 3

# 從第幾頁開始爬（預設 1 = 從頭開始，若中途斷掉可改成續爬的頁碼）
START_FROM_PAGE = 1

# ============================================================
#  以下不需要修改
# ============================================================


def fetch_page(scraper, url, retries=3):
    """抓取頁面，含重試機制"""
    for attempt in range(retries):
        try:
            response = scraper.get(url, timeout=20)
            response.encoding = "utf-8"
            if response.status_code == 200:
                return response.text
            else:
                print(f"  [!] Status {response.status_code}, retry {attempt+1}/{retries}...")
                time.sleep(5)
        except Exception as e:
            print(f"  [!] Error: {e}, retry {attempt+1}/{retries}...")
            time.sleep(5)
    return None


def parse_chapter(html):
    """
    解析頁面正文。
    對應 XPath: //*[@id="sticky-parent"]/div[2]/div[4]
    即 CSS: #sticky-parent > .chapter-detail > .content
    """
    soup = BeautifulSoup(html, "lxml")

    # 章節標題
    title_div = soup.select_one("#sticky-parent .chapter-detail .name")
    title = title_div.get_text(strip=True) if title_div else "（無標題）"

    # 正文內容
    content_div = soup.select_one("#sticky-parent .chapter-detail .content")
    if content_div:
        for br in content_div.find_all("br"):
            br.replace_with("\n")
        content = content_div.get_text()
        # 清理多餘空白行
        lines = content.split("\n")
        cleaned_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped:
                cleaned_lines.append(stripped)
            elif cleaned_lines and cleaned_lines[-1] != "":
                cleaned_lines.append("")
        content = "\n".join(cleaned_lines)
    else:
        content = ""

    return title, content


def get_all_chapter_urls(scraper, novel_url):
    """從目錄頁取得所有章節的 URL 列表"""
    print(f"  正在讀取目錄頁: {novel_url}")
    html = fetch_page(scraper, novel_url)
    if not html:
        print("  [X] 無法讀取目錄頁！")
        return [], ""

    soup = BeautifulSoup(html, "lxml")

    # 取得小說名稱
    novel_name_tag = soup.select_one(".novel-detail .name")
    novel_name = novel_name_tag.get_text(strip=True) if novel_name_tag else "未知小說"

    # 取得所有章節連結
    chapters = soup.select("ul.nav.chapter-list a")
    urls = []
    for ch in chapters:
        href = ch.get("href", "")
        if href.startswith("//"):
            urls.append("https:" + href)
        elif href.startswith("/"):
            urls.append("https://czbooks.net" + href)
        elif href.startswith("http"):
            urls.append(href)

    return urls, novel_name


def scrape_novel():
    """主要爬取流程"""
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), OUTPUT_FILE)

    print()
    print("=" * 60)
    print("  🍤 甜蝦小說爬蟲 - czbooks.net")
    print("=" * 60)

    # 建立 cloudscraper session（繞過 Cloudflare）
    scraper = cloudscraper.create_scraper()

    # 從目錄頁取得所有章節 URL
    all_urls, novel_name = get_all_chapter_urls(scraper, NOVEL_URL)
    total = len(all_urls)

    if total == 0:
        print("  [X] 找不到任何章節！請確認網址是否正確。")
        return

    print(f"  小說名稱: {novel_name}")
    print(f"  總頁數:   {total} 頁")
    print(f"  起始頁:   第 {START_FROM_PAGE} 頁")
    print(f"  每頁延遲: {DELAY_SECONDS} 秒")
    print(f"  輸出檔案: {output_path}")
    print("=" * 60)
    print()

    # 決定寫入模式：從頭開始 = 覆寫，續爬 = 附加
    write_mode = "w" if START_FROM_PAGE == 1 else "a"

    success_count = 0
    fail_count = 0

    with open(output_path, write_mode, encoding="utf-8") as f:
        for i in range(START_FROM_PAGE - 1, total):
            page_num = i + 1
            url = all_urls[i]

            print(f"  [{page_num}/{total}] 正在抓取...")

            html = fetch_page(scraper, url)
            if not html:
                print(f"  [{page_num}] [X] 抓取失敗，跳過此頁。")
                fail_count += 1
                continue

            title, content = parse_chapter(html)

            # 如果內容為空，嘗試重建 session 再抓一次
            if not content:
                print(f"  [{page_num}] [!] 內容為空，重建連線中...")
                scraper = cloudscraper.create_scraper()
                time.sleep(5)
                html = fetch_page(scraper, url)
                if html:
                    title, content = parse_chapter(html)

            # 寫入檔案
            f.write(f"{title}\n")
            f.write("=" * 50 + "\n\n")
            f.write(content if content else "（內容暫時無法取得）")
            f.write("\n\n" + "-" * 50 + "\n\n")
            f.flush()

            success_count += 1
            print(f"  [{page_num}/{total}] {title} ({len(content)} 字) - OK")

            # 等待，避免太頻繁
            time.sleep(DELAY_SECONDS)

    print()
    print("=" * 60)
    print(f"  ✅ 爬取完成！")
    print(f"  成功: {success_count} 頁")
    if fail_count > 0:
        print(f"  失敗: {fail_count} 頁")
    print(f"  輸出: {output_path}")
    print("=" * 60)
    print()


if __name__ == "__main__":
    scrape_novel()
