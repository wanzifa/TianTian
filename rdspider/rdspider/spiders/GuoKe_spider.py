#coding:utf-8

import scrapy
from scrapy.spiders import Spider
from scrapy.http.request import Request
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from ..items import GuoKeItem
#from ..items import GuoKeItem
import requests
from bs4 import BeautifulSoup
from scrapy.linkextractors.sgml import SgmlLinkExtractor as sle
#from scrapy.spiders import Rule
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
#from scrapy.linkextractors import LinkExtractor
import time


class GuoKeSpider(Spider):
    name = 'GuoKeSpider'
    allowed_domains = ['guokr.com']
    response = requests.get('http://www.guokr.com')
    soup = BeautifulSoup(response.content, 'lxml')
    site_tech = soup.find_all('div', class_='contents-l')[1].div.ul.li.a['href']
    path_tech = '/'.join(site_tech.split('/')[-3:-1])
    #site_tech = sel.xpath("//div[@class='contents-l'][1]/div/ul/li/a/@href").extract()
    start_urls = [
        'http://www.guokr.com'
    ]

    # rules = (
            # Rule(sle(allow=('^/$',)), callback='parse_one'),
    #  Rule(sle(allow=('post/725465',)), callback='parse_item'),
    #)
    
    #def start_requests(self):
       # yield scrapy.Request('http://www.guokr.com', self.parse)
       # yield scrapy.Request(self.site_tech, self.parse_item)

    def parse(self, response):
        self.log('heiheihei')
        #self.site_tech =  soup.find_all('div', class_='contents-l')[1].div.ul.li.a['href']
        sel = Selector(text=response.body)
        #title = 'heihei'
        site_tech = sel.xpath("//div[@class='contents-l'][2]/div[1]/ul[1]/li[1]/a/@href").extract()[0]
        title  = sel.xpath("//div[@class='contents-l'][2]/div[1]/ul[1]/li[1]/div[@class='cont'][1]/h3[1]/a/text()").extract()
        return Request(url=site_tech, callback=self.parse_item, meta={'title':title})

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        sel = Selector(text=response.body)
        guoke_tech=GuoKeItem()
        guoke_tech['title'] = response.meta.get('title')
        guoke_tech['author'] = sel.xpath("//a[@id='articleAuthor'][1]/text()").extract()
        guoke_tech['time'] = str(sel.xpath("//p[@class='gfr'][1]/text()").extract())
        guoke_tech['author_url'] = sel.xpath("//a[@id='articleAuthor'][1]/@href").extract()
        guoke_tech['content'] = sel.xpath("//div[@id='articleContent'][1]").extract()
        return guoke_tech
