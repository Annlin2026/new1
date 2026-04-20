# 🐍 Python 程式語言 — 考試重點筆記
> 佔比：**20%** ｜ 優先度：⭐⭐

---

## 一、基本語法

### 變數與資料型別
```python
# 數值
age = 25              # int（整數）
height = 170.5        # float（浮點數）

# 字串
name = "Ann"          # str（字串）

# 布林
is_student = True     # bool（布林值：True / False）

# 查看型別
print(type(age))      # <class 'int'>
```

### 型別轉換
```python
int("123")       # 字串 → 整數 = 123
float("3.14")    # 字串 → 浮點數 = 3.14
str(100)         # 整數 → 字串 = "100"
bool(0)          # 0 → False，其他數字 → True
```

---

## 二、運算子

| 類型 | 運算子 | 範例 |
|------|--------|------|
| 算術 | `+`, `-`, `*`, `/`, `//`, `%`, `**` | `7 // 2 = 3`（整除）、`2**3 = 8`（次方） |
| 比較 | `==`, `!=`, `>`, `<`, `>=`, `<=` | `5 == 5` → `True` |
| 邏輯 | `and`, `or`, `not` | `True and False` → `False` |
| 成員 | `in`, `not in` | `"a" in "apple"` → `True` |

> ⚠️ Python 用 `==` 比較值，用 `is` 比較記憶體位置

---

## 三、流程控制

### if / elif / else
```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")       # ← 輸出 B
elif score >= 70:
    print("C")
else:
    print("F")
```

### for 迴圈
```python
# 遍歷列表
fruits = ["蘋果", "香蕉", "橘子"]
for fruit in fruits:
    print(fruit)

# 使用 range
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8（步長 2）
    print(i)
```

### while 迴圈
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### break 與 continue
```python
for i in range(10):
    if i == 3:
        continue    # 跳過本次，繼續下一次
    if i == 7:
        break       # 直接結束整個迴圈
    print(i)        # 輸出：0, 1, 2, 4, 5, 6
```

---

## 四、資料結構（必考！）

### List（列表）— 有序、可修改、可重複
```python
fruits = ["蘋果", "香蕉", "橘子"]
fruits.append("西瓜")       # 新增元素
fruits.remove("香蕉")       # 移除元素
fruits[0]                    # 取得第一個元素 = "蘋果"
fruits[-1]                   # 取得最後一個元素
len(fruits)                  # 長度
fruits.sort()                # 排序
```

### Tuple（元組）— 有序、不可修改
```python
point = (3, 5)
x = point[0]     # 可以讀取
# point[0] = 10  # ❌ 錯誤！不能修改
```

### Dict（字典）— 鍵值對、無序
```python
student = {
    "name": "Ann",
    "age": 25,
    "city": "台北"
}
student["name"]              # "Ann"
student["email"] = "ann@x"   # 新增
student.keys()               # 所有鍵
student.values()             # 所有值
student.items()              # 所有鍵值對
```

### Set（集合）— 無序、不重複
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b    # 聯集 {1, 2, 3, 4, 5, 6}
a & b    # 交集 {3, 4}
a - b    # 差集 {1, 2}
```

### 四大資料結構比較

| 特性 | List | Tuple | Dict | Set |
|------|------|-------|------|-----|
| 符號 | `[]` | `()` | `{}` | `{}` |
| 有序 | ✅ | ✅ | ❌ | ❌ |
| 可修改 | ✅ | ❌ | ✅ | ✅ |
| 可重複 | ✅ | ✅ | 鍵不可 | ❌ |
| 索引存取 | ✅ | ✅ | 用鍵 | ❌ |

---

## 五、函數（Function）

### 定義與呼叫
```python
def greet(name, greeting="你好"):
    """這是一個打招呼的函數"""
    return f"{greeting}, {name}!"

result = greet("Ann")           # "你好, Ann!"
result = greet("Ann", "嗨")     # "嗨, Ann!"
```

### *args 與 **kwargs
```python
def total(*args):           # 接收任意數量的參數
    return sum(args)

total(1, 2, 3)              # 6

def info(**kwargs):          # 接收任意數量的關鍵字參數
    for k, v in kwargs.items():
        print(f"{k}: {v}")

info(name="Ann", age=25)
```

### Lambda 匿名函數
```python
square = lambda x: x ** 2
square(5)   # 25

# 常搭配 map, filter 使用
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))   # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x%2==0, numbers)) # [2, 4]
```

---

## 六、List Comprehension（列表推導式）

```python
# 傳統寫法
squares = []
for x in range(10):
    squares.append(x**2)

# 推導式（一行搞定）
squares = [x**2 for x in range(10)]

# 帶條件
evens = [x for x in range(20) if x % 2 == 0]
```

---

## 七、檔案讀寫

```python
# 寫入檔案
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Ann!\n")

# 讀取檔案
with open("output.txt", "r", encoding="utf-8") as f:
    content = f.read()        # 讀全部
    # lines = f.readlines()   # 讀成列表（一行一個元素）
```

> 💡 **`with` 語法**：會自動關閉檔案，不需要手動 `f.close()`

### 模式
| 模式 | 說明 |
|------|------|
| `"r"` | 讀取（預設） |
| `"w"` | 寫入（覆蓋） |
| `"a"` | 附加（不覆蓋） |
| `"rb"` | 讀取二進位檔案 |

---

## 八、例外處理

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以零！")
except Exception as e:
    print(f"發生錯誤：{e}")
finally:
    print("不管有沒有錯誤都會執行")
```

---

## 九、常用套件

### pandas — 資料分析神器
```python
import pandas as pd

# 建立 DataFrame
df = pd.DataFrame({
    "姓名": ["Ann", "Bob", "Carol"],
    "分數": [90, 75, 85],
    "城市": ["台北", "高雄", "台北"]
})

# 基本操作
df.head()                # 前 5 筆
df.shape                 # (3, 3) = 3列3欄
df.describe()            # 統計摘要
df["分數"].mean()        # 平均分數
df[df["分數"] > 80]      # 篩選分數 > 80

# 讀取 CSV
df = pd.read_csv("data.csv")
df.to_csv("output.csv", index=False)
```

### matplotlib — 繪圖
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)
plt.title("Sales Chart")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()
```

---

## 十、常見考題速記

| 題型 | 重點 |
|------|------|
| `list` vs `tuple` | list 可改、tuple 不可改 |
| `==` vs `is` | `==` 比值、`is` 比記憶體位置 |
| `range(5)` 產生什麼 | 0, 1, 2, 3, 4（不包含 5） |
| 字典取值 | `dict["key"]` 或 `dict.get("key", default)` |
| `with open` 的好處 | 自動關閉檔案 |
| lambda 是什麼 | 一行的匿名函數 |
| pandas 讀 CSV | `pd.read_csv("file.csv")` |

---

*📝 by 甜蝦 🍤 | 2026.04.20*
