#coding:utf-8

from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from ..items import HuxiuItem
import logging

class HuxiuSpider(Spider):
    name = 'Huxiu'
    allowed_domains = ['huxiu.com']
    start_urls = ['http://www.huxiu.com/whatsnew.html']

    def parse(self, response):
        logging.info('Hi, this is the main page!')
        sel = Selector(text=response.body)
        title_big = sel.xpath("//div[@class='big2-pic-right pull-right']/div[1]/a/text()").extract()[0]
        href_big = 'http://www.huxiu.com' + sel.xpath("//div[@class='big2-pic-right pull-right']/div[1]/a/@href").extract()[0]
        yield Request(url=href_big, callback=self.parse_item, meta={'title':title_big})
        post_list = sel.xpath("//div[@class='mod-info-flow']/div[@class='mod-b mod-art']").extract()
        for post in post_list:
            post = Selector(text=post)
            title = post.xpath("//div[1]/div[1]/a/img/@alt").extract()[0]
            href = 'http://www.huxiu.com' + post.xpath("//div[1]/div[1]/a/@href").extract()[0]
            yield Request(url=href, callback=self.parse_item, meta={'title':title})

    def parse_item(self, response):
        logging.info('Hi, this is an item page! %s' % response.url)
        sel = Selector(text=response.body)
        Huxiu = HuxiuItem()
        Huxiu['name'] = 'huxiu'
        Huxiu['title'] = response.meta.get('title')
        Huxiu['author'] = sel.xpath("//div[@class='article-author']/span[1]/a/text()").extract()[0]
        Huxiu['author_url'] = 'http://www.huxiu.com' + sel.xpath("//div[@class='article-author']/span[1]/a/@href").extract()[0]
        Huxiu['time'] = sel.xpath("//span[@class='article-time']/text()").extract()[0]
        Huxiu['content'] = sel.xpath("//div[@id='article_content']").extract()[0]
        Huxiu['category'] = '24小时快讯'
        return Huxiu





        

