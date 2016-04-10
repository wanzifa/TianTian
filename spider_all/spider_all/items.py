# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuoKeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()
    author_url = scrapy.Field()
    category = scrapy.Field()


class HuxiuItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    author_url = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    category = scrapy.Field()

class DoubanItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    author_url = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    book_name = scrapy.Field()
    book_url = scrapy.Field()

class ZhihuItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    author_url = scrapy.Field()
    time = scrapy.Field()
    category = scrapy.Field()
