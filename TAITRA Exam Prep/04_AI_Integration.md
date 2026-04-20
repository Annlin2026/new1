# 🤖 AI 整合應用 (Agent/MCP/Tools/Skills) — 考試重點筆記
> 佔比：**15%** ｜ 優先度：⭐

---

## 一、AI Agent（人工智慧代理）

### 什麼是 AI Agent？
傳統的 AI（如早期的 ChatGPT）只能「你問我答」。
**AI Agent** 則是具備「**自主性**」的系統，它不僅能對話，還能**感知環境、思考規劃、並採取行動**來完成複雜任務。

### Agent 的三大核心能力（運作架構）
| 核心 | 英文 | 說明 |
|------|------|------|
| **感知** | Perception | 接收輸入，例如：讀取使用者的訊息、查看目前開啟的檔案、了解電腦狀態。 |
| **思考/規劃** | Planning / Brain | 分析任務、拆解步驟、決定需要呼叫什麼工具、思考解決方案。 |
| **行動** | Action | 呼叫外部工具（如執行程式碼、寫入檔案、搜尋網路）來改變環境。 |

> 💡 **甜蝦比喻**：
> - 傳統 AI 是一本百科全書（只能查資料）。
> - AI Agent 是一個實習生（你給他任務，他會自己規劃步驟並去執行）。

---

## 二、MCP (Model Context Protocol) 模型上下文協定

### 什麼是 MCP？
MCP 是一種**標準化通訊協定**。它定義了 AI 模型（Model）如何與外部資料來源或工具（Context）進行安全、統一的溝通。

### 為什麼需要 MCP？
以前，每個 AI 應用如果要連接本地檔案、GitHub 或資料庫，都需要寫客製化的整合程式碼。
MCP 提供了一個標準介面，讓 AI 可以**隨插即用**地存取各種外部資源，就像 USB 隨身碟一樣，插上去就能讀取資料。

### MCP 的架構
- **MCP Client（客戶端）**：例如 Claude Desktop、Antigravity，是發起請求的一方。
- **MCP Server（伺服器端）**：提供資源或工具的一方（例如：一個專門讀取 Google Drive 的 MCP Server）。
- **Protocol（協定）**：兩者之間透過標準化的 JSON 格式交換訊息。

---

## 三、Tools（工具）與 Function Calling（函數呼叫）

### 什麼是 Tools？
AI 本身只是一個「大腦」，沒有手腳。**Tools（工具）就是 AI 的手腳**。透過工具，AI 可以與外部世界互動。

### 常見的 Tools 範例
- **檔案操作**：`read_file`, `write_to_file`, `list_directory`
- **終端機/命令列**：`run_command`（讓 AI 能執行 PowerShell 指令）
- **網路存取**：`search_web`, `read_url`
- **程式執行**：讓 AI 執行 Python 腳本並獲取結果

### Function Calling 的運作流程（必考！）
1. **宣告（Declaration）**：系統預先告訴 AI 有哪些函數（Tools）可用，以及每個函數的參數格式。
2. **決策（Decision）**：AI 收到使用者請求後，判斷是否需要呼叫函數。
3. **呼叫（Tool Call）**：AI 輸出特定格式（如 JSON），要求系統執行該函數，並提供必要參數。
4. **執行（Execution）**：系統在背景執行函數。
5. **回傳（Response）**：系統將函數執行的結果（Tool Response）傳回給 AI。
6. **總結（Final Output）**：AI 根據結果生成最終回答給使用者。

---

## 四、Skills（技能）

### 什麼是 Skills？
Skills 是一種**可重複使用的知識或流程模組**。它把解決特定問題的經驗記錄下來，讓 AI 下次遇到類似任務時，可以直接調用，而不用從零開始摸索。

### Skills 的好處
- **減少重複試錯**：避免每次都踩一樣的坑（例如：一直被 Cloudflare 擋）。
- **個人化**：記錄使用者的特定偏好或專案的特定架構。
- **提升效率**：讓 AI 能快速進入狀況，直接給出最佳解法。

> 💡 **就像是給 AI 吃的「記憶吐司」或「操作手冊」**。

---

## 五、Prompt Engineering 基礎（提示詞工程）

### 寫好 Prompt 的原則
1. **明確具體**：避免模糊不清的指令。
2. **提供上下文**：給予 AI 充足的背景資訊（Context）。
3. **指定角色/語氣**：例如「你是一位專業的資料科學家...」。
4. **給予範例（Few-shot prompting）**：提供輸入輸出的範例，讓 AI 照著做。
5. **指定輸出格式**：要求以 Markdown、JSON、表格等特定格式輸出。

### RAG (Retrieval-Augmented Generation) 檢索增強生成
- **定義**：在讓 AI 回答問題之前，先去外部資料庫（如企業內部文件）**檢索（Retrieve）** 相關資訊，把這些資訊加入 Prompt 中（Augmented），再讓 AI **生成（Generate）** 回答。
- **目的**：解決 AI 幻覺（胡說八道）的問題，讓 AI 能根據最新、最準確的內部資料回答。

---

## 常見考題速記

| 題型關鍵字 | 對應概念 |
|------------|----------|
| 具備自主規劃與執行任務能力的系統 | AI Agent |
| 標準化 AI 與外部資料溝通的協定 | MCP (Model Context Protocol) |
| 讓 AI 能夠執行外部程式或讀寫檔案的機制 | Tools / Function Calling |
| 將解決問題的經驗與流程記錄下來供 AI 重複使用 | Skills |
| 解決 AI 幻覺，結合外部知識庫的技術 | RAG (檢索增強生成) |
| Agent 的三大核心步驟 | 感知 (Perception) → 思考 (Planning) → 行動 (Action) |

---

*📝 by 甜蝦 🍤 | 2026.04.20*
