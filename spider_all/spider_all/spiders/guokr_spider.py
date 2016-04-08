#coding:utf-8
import scrapy
from scrapy.spiders import Spider
from scrapy.http.request import Request
from scrapy.selector import Selector
from ..items import GuoKeItem
from bs4 import BeautifulSoup
from selenium import webdriver


class GuoKeSpider(Spider):
    name = 'GuoKeSpider'
    allowed_domains = ['guokr.com']
    start_urls = [
        'http://www.guokr.com'
    ]
    
    def parse(self, response):
        sel = Selector(text=response.body)
        soup = BeautifulSoup(response.body, 'lxml')
        sel_tech_life = sel.xpath("//div[@class='contents gclear'][2]/div[@class='contents-l']/div[@class='content']/ul[1]/li").extract()         
        sel_fun = None
        i=0
        for item in sel_tech_life:
            item = Selector(text=item)
            if i>=8:
                category = '生活'
            else:
                category = '科技'
            if item.xpath("//a[1]/img[1]/@alt"):
                title = item.xpath("//a[1]/img[1]/@alt").extract()[0]
            else:
                title = item.xpath("//a[1]/text()").extract()[0]
            site = item.xpath('//a[1]/@href').extract()[0]
            i = i + 1
            yield Request(url=site, callback=self.parse_item, meta={'title':title, 'category':category})
    
    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        browser = webdriver.Firefox()
        browser.get(response.url)
        PageSource = browser.page_source
        sel = Selector(text=PageSource)
        guoke=GuoKeItem()
        guoke['name'] = 'guoke'
        guoke['title'] = response.meta.get('title')
        guoke['author'] = sel.xpath("//a[@id='articleAuthor'][1]/text()").extract()
        guoke['time'] = sel.xpath("//p[@class='gfr'][1]/text()").extract()
        guoke['author_url'] = sel.xpath("//a[@id='articleAuthor'][1]/@href").extract()
        guoke['content'] = sel.xpath("//div[@id='articleContent']").extract()
        guoke['category'] = response.meta.get('category')
        browser.quit()
        return guoke
