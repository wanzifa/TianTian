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
    
    # 本想用模拟登陆掩饰一下抓不了ajax页面的尴尬
    # 然而并没有用
    # hhhh
    """
    headers = {
            "Host": 'www.guokr.com',
            "Accept": "*/*",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
            "Connection": "keep-alive",
            "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "http://www.guokr.com",
            "Origin": "http://www.guokr.com"
    }
    """

    def parse(self, response):
        sel = Selector(text=response.body)
        soup = BeautifulSoup(response.body, 'lxml')
        #print soup
        #print r.url
        #print sel
        sel_tech_life = sel.xpath("//div[@class='contents gclear'][2]/div[@class='contents-l']/div[@class='content']/ul[1]/li").extract()         
        #print Selector(text=sel_tech[0])
        #sel_life = sel.xpath("//div[@class='contents gclear'][2]/div[@class='contents-l']/div[@class='content'][2]/ul[1]/li").extract()
        #sel_human = sel.xpath
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
            yield Request(url=site, headers=self.headers,callback=self.parse_item, meta={'title':title, 'category':category})
    
        """
        for item in sel_tech_life:
            item = Selector(text=item)
            category = item.xpath("//h2[1]/text()").extract()[0]
            for subitem in item.xpath("//ul[1]/li").extract():
                subitem = Selector(text=subitem)
                if item.xpath("//a[1]/img[1]/@alt"):
                    title = item.xpath("//a[1]/img[1]/@alt").extract()[0]
                else:
                    title = item.xpath("//a[1]/text()").extract()[0]
                site = item.xpath("//a[1]/@href").extract()[0]
                yield Request(url=site, callback=self.parse_item, meta={'title':title, 'category':category})
        """

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        browser = webdriver.Firefox()
        browser.get(response.url)
        PageSource = browser.page_source
        sel = Selector(text=PageSource)
        guoke=GuoKeItem()
        image=ImageItem()
        guoke['title'] = response.meta.get('title')
        guoke['author'] = sel.xpath("//a[@id='articleAuthor'][1]/text()").extract()
        guoke['time'] = sel.xpath("//p[@class='gfr'][1]/text()").extract()
        guoke['author_url'] = sel.xpath("//a[@id='articleAuthor'][1]/@href").extract()
        guoke['content'] = sel.xpath("//div[@id='articleContent']").extract()
        guoke['category'] = response.meta.get('category')
       # print browser.page_source
        browser.quit()
        return guoke
        
