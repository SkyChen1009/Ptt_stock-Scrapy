# Ptt_stock-Scrapy

### PTT Stock Forum 爬蟲

這個爬蟲程式是用來抓取 PTT 股市板（Stock）的文章資料。爬蟲會遍歷指定頁數的文章，提取文章的標題、作者、發佈日期、推文數量以及文章中的留言內容。

## 功能

- 從 PTT 股市板抓取多頁的文章資料。
- 提取每篇文章的以下資訊：
  - 標題
  - 作者
  - 發佈日期
  - 推文數量
  - 文章的 URL
- 進入每篇文章頁面，提取該文章的留言內容。
- 把每篇文章的詳細資料（包括留言）輸出。

## 安裝與使用

### 安裝 Scrapy

在使用爬蟲前，你需要安裝 [Scrapy](https://scrapy.org/)，可以使用以下命令進行安裝：

```bash
pip install scrapy
```

### 設置專案
使用 Scrapy 初始化一個新專案：

```bash
scrapy startproject ptt_stock
```

把此爬蟲程式保存為 ptt_stock_spider.py 並放入 ptt_stock/spiders 資料夾中。

創建一個名為 items.py 的檔案，並定義資料結構。範例如下：

```python
import scrapy

class PttStockItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    push = scrapy.Field()
    url = scrapy.Field()
    comments = scrapy.Field()

```

### 運行爬蟲

在專案的根目錄下，運行以下命令來啟動爬蟲：

```bash
scrapy crawl ptt_stock -o output.json
```

這個命令會啟動爬蟲，並將抓取的資料儲存為 output.json 文件。你也可以根據需要更改輸出的格式，例如 CSV 或 XML。

## 輸出格式
### 爬蟲會輸出以下欄位：

- url：文章的 URL
- title：文章的標題
- author：文章的作者
- date：文章的發佈日期
- push：文章的推文數量
- comments：文章的留言內容

### 輸出範例

以下是輸出的 JSON 格式範例：

```json
{
  "url": "https://www.ptt.cc/bbs/Stock/M.1234567890.A.BCD.html",
  "title": "股票市場分析",
  "author": "stockmaster",
  "date": "2024-12-20",
  "push": "20",
  "comments": [
    "這篇文章寫得很好！",
    "我同意，這個分析很有道理！"
  ]
}
```

## 注意事項

- 在使用本爬蟲程式時，請確保遵守 PTT 的使用規範，避免過度請求導致封鎖。
- 本爬蟲程式會模擬點選「滿18歲」的選項，來允許抓取成人內容。

### 開發者
本程式由 SkyChen1009 開發。
