import requests
from scrapy.selector import Selector
from scrapy.spiders import Spider
from ..items import DoubanItem
from scrapy.http.request import Request
class DoubanSpider(Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['http://www.baidu.com']

    def parse(self,response):
        douban = requests.get('https://book.douban.com/review/best/')
        sel_db = Selector(text=douban.content)
        for post in sel_db.xpath("//div[@class='tlst']").extract():
            post_sel = Selector(text=post)
            post_title = post_sel.xpath("//div[@class='nlst'][1]/h3/a/text()").extract()[0]
            post_url = post_sel.xpath("//div[@class='nlst'][1]/h3/a/@href").extract()[0]
            post_response = requests.get(post_url)
            yield self.parse_item(post_response,post_title)

    def parse_item(self, response, title):
        douban = DoubanItem()
        sel = Selector(text=response.content)
        douban['title'] = title
        douban['time'] = sel.xpath("//span[@class='mn']/text()").extract()[0]
        douban['author'] = sel.xpath("//span[@property='v:reviewer']/text()").extract()[0]
        douban['author_url'] = sel.xpath("//span[@class='pl2']/a[1]/@href").extract()[0]
        douban['book_name'] = sel.xpath("////span[@property='v:itemreviewed']/text()").extract()[0]
        douban['book_url'] = sel.xpath("//span[@class='pl2']/a[2]/@href").extract()[0]
        douban['content'] = sel.xpath("//div[@class='review-text']").extract()[0]
        douban['name'] = 'douban'
        return douban

        
