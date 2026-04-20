# 📊 SQL 資料庫查詢語言 — 考試重點筆記
> 佔比：**30%** ｜ 優先度：⭐⭐⭐ 最高

---

## 一、SQL 語言分類

| 分類 | 全名 | 用途 | 常見指令 |
|------|------|------|----------|
| **DDL** | Data Definition Language | 定義資料結構 | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML** | Data Manipulation Language | 操作資料內容 | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |
| **DCL** | Data Control Language | 權限控制 | `GRANT`, `REVOKE` |
| **TCL** | Transaction Control Language | 交易控制 | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

> 💡 **口訣**：DDL 管結構、DML 管資料、DCL 管權限、TCL 管交易

---

## 二、SELECT 查詢語法（最常考！）

### 基本語法結構
```sql
SELECT 欄位1, 欄位2        -- 要顯示的欄位
FROM 資料表                  -- 從哪個表
WHERE 條件                   -- 篩選條件
GROUP BY 分組欄位            -- 分組
HAVING 分組後條件            -- 分組後再篩選
ORDER BY 排序欄位 ASC/DESC   -- 排序
LIMIT 數量                   -- 限制筆數
```

### ⚠️ 執行順序（很重要！和寫的順序不同）
```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

> 💡 **口訣**：**F**rom **W**here **G**roup **H**aving **S**elect **O**rder **L**imit
> 「**富婆** **我** **哥** **很** **帥** **噢** **溜**」

---

## 三、WHERE 條件運算子

| 運算子 | 說明 | 範例 |
|--------|------|------|
| `=`, `!=`, `<>` | 等於、不等於 | `WHERE age = 25` |
| `>`, `<`, `>=`, `<=` | 比較 | `WHERE salary >= 50000` |
| `AND`, `OR`, `NOT` | 邏輯組合 | `WHERE age > 20 AND city = '台北'` |
| `BETWEEN` | 介於之間 | `WHERE age BETWEEN 20 AND 30` |
| `IN` | 在列表中 | `WHERE city IN ('台北', '高雄')` |
| `LIKE` | 模糊搜尋 | `WHERE name LIKE '林%'` |
| `IS NULL` / `IS NOT NULL` | 空值判斷 | `WHERE email IS NOT NULL` |

### LIKE 萬用字元
| 符號 | 意義 | 範例 | 匹配 |
|------|------|------|------|
| `%` | 任意多個字元 | `'林%'` | 林小明、林大大 |
| `_` | 任意一個字元 | `'林_明'` | 林小明（不含林大大明） |

---

## 四、聚合函數（Aggregate Functions）

| 函數 | 功能 | 範例 |
|------|------|------|
| `COUNT(*)` | 計算筆數 | `SELECT COUNT(*) FROM employees` |
| `SUM(欄位)` | 加總 | `SELECT SUM(salary) FROM employees` |
| `AVG(欄位)` | 平均 | `SELECT AVG(salary) FROM employees` |
| `MAX(欄位)` | 最大值 | `SELECT MAX(salary) FROM employees` |
| `MIN(欄位)` | 最小值 | `SELECT MIN(salary) FROM employees` |

> ⚠️ **注意**：`COUNT(*)` 包含 NULL，`COUNT(欄位)` 不包含 NULL

---

## 五、GROUP BY 與 HAVING

### GROUP BY — 分組統計
```sql
-- 統計每個部門的人數
SELECT department, COUNT(*) AS 人數
FROM employees
GROUP BY department;
```

### HAVING — 分組後再篩選
```sql
-- 找出人數超過 10 人的部門
SELECT department, COUNT(*) AS 人數
FROM employees
GROUP BY department
HAVING COUNT(*) > 10;
```

> ⚠️ **WHERE vs HAVING 差異**：
> - `WHERE`：在分組**之前**篩選（過濾原始資料）
> - `HAVING`：在分組**之後**篩選（過濾聚合結果）

---

## 六、JOIN 表格連接（必考！）

### 四種 JOIN 類型

```
      A 表          B 表

  ┌─────────┐   ┌─────────┐
  │         │   │         │
  │    A  ┌─┼───┼─┐  B    │
  │       │ │   │ │       │
  │       │交│   │集│       │
  │       └─┼───┼─┘       │
  │         │   │         │
  └─────────┘   └─────────┘
```

| JOIN 類型 | 說明 | 結果 |
|-----------|------|------|
| `INNER JOIN` | 交集 | 只回傳兩表都有匹配的資料 |
| `LEFT JOIN` | 左表全部 + 右表匹配 | 左表全部保留，右表沒匹配的填 NULL |
| `RIGHT JOIN` | 右表全部 + 左表匹配 | 右表全部保留，左表沒匹配的填 NULL |
| `FULL OUTER JOIN` | 聯集 | 兩表全部保留，沒匹配的填 NULL |

### 範例
```sql
-- INNER JOIN：找出有部門的員工
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id;

-- LEFT JOIN：列出所有員工（包含沒部門的）
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id;
```

> 💡 **口訣**：INNER 取交集、LEFT 留左邊、RIGHT 留右邊、FULL 全都留

---

## 七、子查詢（Subquery）

### 在 WHERE 中使用
```sql
-- 找出薪水高於平均的員工
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

### 搭配 IN 使用
```sql
-- 找出在台北分部工作的員工
SELECT name
FROM employees
WHERE dept_id IN (SELECT id FROM departments WHERE city = '台北');
```

### 搭配 EXISTS 使用
```sql
-- 找出有訂單的客戶
SELECT name
FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);
```

> 💡 **IN vs EXISTS**：
> - `IN`：適合子查詢結果集較小時
> - `EXISTS`：適合子查詢結果集較大時（效率較高）

---

## 八、CASE WHEN 條件表達式

```sql
-- 根據薪水分級
SELECT name, salary,
    CASE
        WHEN salary >= 80000 THEN '高薪'
        WHEN salary >= 50000 THEN '中薪'
        ELSE '低薪'
    END AS 薪資等級
FROM employees;
```

---

## 九、DDL 資料定義

### CREATE TABLE
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10, 2) DEFAULT 0,
    dept_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dept_id) REFERENCES departments(id)
);
```

### 常見約束條件
| 約束 | 說明 |
|------|------|
| `PRIMARY KEY` | 主鍵，唯一且不可 NULL |
| `FOREIGN KEY` | 外鍵，參照其他表的主鍵 |
| `NOT NULL` | 不可為空 |
| `UNIQUE` | 唯一值 |
| `DEFAULT` | 預設值 |
| `CHECK` | 檢查條件 |

### ALTER TABLE
```sql
ALTER TABLE employees ADD COLUMN phone VARCHAR(20);    -- 新增欄位
ALTER TABLE employees DROP COLUMN phone;               -- 刪除欄位
ALTER TABLE employees MODIFY COLUMN name VARCHAR(100); -- 修改欄位
```

---

## 十、DML 資料操作

### INSERT
```sql
INSERT INTO employees (name, email, salary)
VALUES ('林小明', 'ming@example.com', 55000);
```

### UPDATE
```sql
UPDATE employees
SET salary = 60000
WHERE name = '林小明';
```

### DELETE
```sql
DELETE FROM employees
WHERE id = 5;
```

> ⚠️ **DELETE vs TRUNCATE vs DROP**：
> - `DELETE`：刪除特定資料（可回復、可加 WHERE）
> - `TRUNCATE`：清空整張表的資料（不可回復、更快）
> - `DROP`：直接刪除整張表（結構也刪掉）

---

## 十一、VIEW 視圖

```sql
-- 建立視圖
CREATE VIEW high_salary_employees AS
SELECT name, salary, department
FROM employees
WHERE salary > 70000;

-- 使用視圖（當成普通表查詢）
SELECT * FROM high_salary_employees;
```

> 💡 視圖 = **虛擬的表**，不會存實際資料，每次查詢都重新執行

---

## 十二、INDEX 索引

```sql
-- 建立索引（加速查詢）
CREATE INDEX idx_employee_name ON employees(name);

-- 建立複合索引
CREATE INDEX idx_dept_salary ON employees(dept_id, salary);
```

> 💡 索引的取捨：
> - ✅ 優點：大幅加速 SELECT 查詢
> - ❌ 缺點：會讓 INSERT/UPDATE/DELETE 變慢（因為要同步更新索引）

---

## 十三、Transaction 交易

```sql
BEGIN TRANSACTION;

UPDATE accounts SET balance = balance - 1000 WHERE id = 1;
UPDATE accounts SET balance = balance + 1000 WHERE id = 2;

COMMIT;  -- 確認交易（兩筆都成功才執行）
-- 或
ROLLBACK; -- 取消交易（任一筆失敗就全部回復）
```

### ACID 特性（必考！）
| 特性 | 英文 | 說明 |
|------|------|------|
| **A** 原子性 | Atomicity | 交易中的操作要嘛全成功、要嘛全失敗 |
| **C** 一致性 | Consistency | 交易前後資料必須維持一致狀態 |
| **I** 隔離性 | Isolation | 多個交易同時進行時互不影響 |
| **D** 持久性 | Durability | 交易完成後的結果會永久保存 |

> 💡 **口訣**：ACID = 酸 → 交易要像「酸」一樣保持穩定不變質

---

## 常見考題速記

| 題型 | 關鍵字 |
|------|--------|
| 查詢某個條件的資料 | SELECT + WHERE |
| 統計每個分類的數量 | GROUP BY + COUNT |
| 找出最大/最小/平均 | MAX / MIN / AVG |
| 兩表合併查詢 | JOIN + ON |
| 過濾聚合結果 | HAVING |
| 判斷空值 | IS NULL / IS NOT NULL |
| 模糊搜尋 | LIKE + % 或 _ |
| 條件分支 | CASE WHEN |
| 巢狀查詢 | 子查詢 (Subquery) |

---

*📝 by 甜蝦 🍤 | 2026.04.20*
