#coding: utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import datetime
import MySQLdb.cursors
import sys
from scrapy import log
import os
import logging

class RdspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class SQLStorePipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', db='mydb',
                user='root', passwd=os.environ.get('MYSQL_PASSWORD'),
                cursorclass=MySQLdb.cursors.DictCursor,
                charset='utf8', use_unicode=True)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert,
                item)
        query.addErrback(self.handler_error)
        return item

    def _conditional_insert(self, tx, item):
        if item['name'] == 'guoke':
            tx.execute(""" 
                   select * from guoke where author=%s and title=%s 
            """,(item['author'],item['title']))
            result = tx.fetchone()
            if result:
                log.msg("Item already stored in db: %s" % item.name,
                    level=log.DEBUG)
            else:
                tx.execute("""
                insert into guoke(title, author, author_url, time, content, category)
                values(%s,%s,%s,%s,%s,%s) 
                """, (item['title'],item['author'],item['author_url'], item['time'], item['content'], item['category']))
                log.msg("Item stored in db: %s" % item, level=log.DEBUG)
        elif item['name'] == 'guoke':
            tx.execute(""" 
                   select * from huxiu where author=%s and title=%s 
            """,(item['author'],item['title']))
            result = tx.fetchone()
            if result:
                log.msg("Item already stored in db: %s" % item.name,
                    level=log.DEBUG)
            else:
                tx.execute("""
                insert into huxiu(title, author, author_url, time, content, category)
                values(%s,%s,%s,%s,%s,%s) 
                """, (item['title'],item['author'],item['author_url'], item['time'], item['content'], item['category']))
                log.msg("Item stored in db: %s" % item, level=log.DEBUG)
   
    def handler_error(self, e):
        log.err(e)


