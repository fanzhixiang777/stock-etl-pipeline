# Stock ETL Pipeline

一條股市資料 ETL pipeline。用 API 從 Alpha Vantage 抓取股票資料，
經過清理轉換後存進 SQLite 資料庫，再用 pandas 計算技術指標
（移動平均、每日漲跌幅、波動度）。

## 技術 (Tech Stack)

- Python
- requests（API 呼叫）
- pandas（資料處理與分析）
- SQLite（資料庫）
- Git / GitHub

## 流程 (Pipeline)

1. **Extract** — 用 requests 打 Alpha Vantage API，取得股價 JSON
2. **Parse** — 從巢狀 JSON 挖出每日 OHLCV 資料
3. **Transform** — 用 pandas 整理成表格、轉換型別、清理欄位
4. **Load** — 存進 SQLite 資料庫
5. **Query / Analysis** — 用 SQL 讀取，再用 pandas 計算技術指標

## 分析指標 (Indicators)

- **MA5** — 5 日移動平均，平滑股價看趨勢
- **Daily Return** — 每日漲跌幅
- **Volatility** — 波動度（每日漲跌幅的標準差），衡量風險