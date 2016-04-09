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
from selenium import webdriver

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
        explore2 = s.get('https://www.zhihu.com/node/ExploreAnswerListV2?params={"offset":5,"type":"day"}')
        sel_explore = Selector(text=explore.content)
        sel_explore2 = Selector(text=explore2.content)
        #爬今日最热前五条
        for i in range(1,6):
            post = sel_explore.xpath("//div[@data-offset='{0}']".format(i)).extract()[0]
            post_sel = Selector(text=post)
            post_title = post_sel.xpath("//h2/a[1]/text()").extract()[0]
            post_category = '今日最热'
            post_url_pre = post_sel.xpath("//h2/a[1]/@href").extract()[0]
            post_url = post_url_pre if post_url_pre.startswith("http") else 'https://www.zhihu.com'+post_url_pre
            post_response = s.get(post_url)
            yield self.parse_item(post_response, post_title, post_category)
        #今日最热往后再爬五条
        for i in range(6,11):
            post2 = sel_explore2.xpath("//div[@data-offset='{0}']".format(i)).extract()[0]
            post_sel2 = Selector(text=post2)
            post_title2 = post_sel2.xpath("//h2/a[1]/text()").extract()[0]
            post_category2 = '今日最热'
            post_url_pre2 = post_sel2.xpath("//h2/a[1]/@href").extract()[0]
            post_url2 = post_url_pre2 if post_url_pre2.startswith("http") else 'https://www.zhihu.com'+post_url_pre2
            post_response2 = s.get(post_url2)
            yield self.parse_item(post_response2, post_title2, post_category2)
    
    def parse_item(self, response, title, category):
        cookie = response.cookies
        browser = webdriver.Firefox()
        browser.get(response.url)
        PageSource = browser.page_source
        sel = Selector(text=response.content)
        zhihu = ZhihuItem()
        sel2 = Selector(text=PageSource)
        zhihu['author'] = sel.xpath("//a[@class='author-link'][1]/text()").extract()[0]
        zhihu['author_url'] = 'https://www.zhihu.com' + sel.xpath("//div[@class='answer-head'][1]/div[@class='zm-item-answer-author-info'][1]/a[@class='author-link'][1]/@href").extract()[0]
        zhihu['title'] = title
        zhihu['category'] = category
        zhihu['content'] = sel2.xpath("//div[@class='zm-editable-content clearfix']").extract()[0]
        print zhihu['content']
        zhihu['time'] = sel.xpath("//span[@class='answer-date-link-wrap'][1]/a[1]/text()").extract()[0]
        browser.quit()
        zhihu['name'] = 'zhihu'
        return zhihu
