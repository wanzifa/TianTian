#coding:utf-8
"""
爬取知乎“发现”页面的10篇文章
"""
import requests
from scrapy.spiders import Spider
from scrapy.selector import Selector
from ..items import ZhihuItem
import os
from scrapy.http.request import Request
from bs4 import BeautifulSoup

class ZhihuSpider(Spider):
    name = "zhihu"
    allowed_domains = ["zhihu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self,response):
        url = "http://www.zhihu.com"
        login_url = "http://www.zhihu.com/login/email"
        header = {'Host':"www.zhihu.com",
                'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
                'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                'Accept-Encoding':"gzip, deflate",
                'X-Requested-With':"XMLHttpRequest",
                'Connection':'keep-alive',
                'Referer': 'https://www.zhihu.com'
        }

        s = requests.session()
        r = s.get(url, headers=header)
        #print r.cookies
        xsrf = r.cookies['_xsrf']
        email = os.environ.get('EMAIL')
        password = os.environ.get('ZHIHU_PASSWORD')
        data = {
                'email':email,
                'password': password,
                '_xsrf':xsrf,
                'remember_me':'true'
        }
        login = s.post(login_url, data=data)
        explore = s.get('https://www.zhihu.com/explore')
        sel_explore = Selector(text=explore.content)
        for post in sel_explore.xpath("//div[@id='zh-recommend-list']/div").extract():
            post_sel = Selector(text=post)
            post_title = post_sel.xpath("//h2/a/text()").extract()[0]
            post_category = '编辑推荐'
            post_url_pre = post_sel.xpath("//h2/a/@href").extract()[0]
            post_url = post_url_pre if post_url_pre.startswith("http") else 'http://www.zhihu.com'+post_url_pre
            post_response = s.get(post_url)
            yield self.parse_item(post_response, post_title, post_category)
 
    def parse_item(self, response, title, category):
        zhihu = ZhihuItem()
        sel = Selector(text=response.content)
        zhihu['title'] = title
        zhihu['category'] = category
        author_pre  = sel.xpath("//a[@class='author-link'][1]/text()").extract()
        if not author_pre:
            zhihu['author'] = sel.xpath("//div[@class='entry-meta']/a[@class='author name ng-binding'][1]/text()").extract()
            print zhihu['author']
            zhihu['author_url'] = sel.xpath("//a[@class='author name ng-binding'][1]/@href").extract()
            zhihu['time'] = sel.xpath("//div[@class='entry-meta'][1]/time[1]/@ui-hover-title").extract()
            print zhihu['time']
    
