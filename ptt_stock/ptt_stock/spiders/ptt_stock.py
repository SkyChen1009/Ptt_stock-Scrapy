from items import PttStockItem
import scrapy
import time

class PTTStockSpider(scrapy.Spider):
    name = 'ptt_stock'
    allowed_domains = ['ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Stock/index.html']

    def parse(self, response):
        # 模擬多頁爬取，從目前的索引頁向前爬取多頁
        for i in range(100):  # 爬取 100 頁的數據
            time.sleep(1)  # 防止過快請求造成封鎖
            url = f"https://www.ptt.cc/bbs/Stock/index{int(8142 - i)}.html"
            yield scrapy.Request(url, cookies={'over18': '1'}, callback=self.parse_page)

    def parse_page(self, response):
        # 解析單頁內的文章列表
        target = response.css("div.r-ent")
        for tag in target:
            item = PttStockItem()
            try:
                # 提取每篇文章的標題、作者、日期、推文數量和 URL
                item['title'] = tag.css("div.title a::text").get()
                item['author'] = tag.css('div.author::text').get()
                item['date'] = tag.css('div.date::text').get()
                item['push'] = tag.css('span.hl::text').get(default='0')  # 預設推文數為 0
                item['url'] = response.urljoin(tag.css('div.title a::attr(href)').get())

                # 傳遞給後續處理，進入文章頁面抓取留言
                post_url = response.urljoin(tag.css('div.title a::attr(href)').get())
                yield scrapy.Request(post_url, cookies={'over18': '1'}, callback=self.parse_post, meta={'item': item})

            except IndexError:
                pass

    def parse_post(self, response):
        # 提取留言邏輯
        item = response.meta['item']  # 取出來的文章資料
        comments = response.css('div.push .push-content::text').getall()
        item['comments'] = comments  # 將留言加入到 item 中

        # 輸出文章的 URL, 標題, 作者, 日期, 推文數量, 留言
        yield {
            'url': item['url'],
            'title': item['title'],
            'author': item['author'],
            'date': item['date'],
            'push': item['push'],
            'comments': item['comments']
        }
