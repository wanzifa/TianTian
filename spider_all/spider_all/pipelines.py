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


class GuoKeStorePipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', db='mydb',
                user='root', passwd='wanzifa',
                cursorclass=MySQLdb.cursors.DictCursor,
                charset='utf8', use_unicode=True)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert,
                item)
        query.addErrback(self.handler_error)
        return item

    def _conditional_insert(self, tx, item):
        tx.execute("""
                select * from guoke  where title = %s and author = %s and time = %s and category = %s 
        """,(item['title'], item['author'], item['time'], item['category']))
        result = tx.fetchone()
        if result:
            log.msg("Item already stored in db: %s" % item,
                    level=log.DEBUG)
        else:
            tx.execute("""
            insert into guoke(title, author, author_url, time, content, category)
            values(%s,%s,%s,%s,%s,%s)
            """, (item['title'],item['author'],item['author_url'], item['time'], item['content'], item['category']))
        # (item['title'],item['author'],item['author_url'],item['time']))
            log.msg("Item stored in db: %s" % item, level=log.DEBUG)

    def handler_error(self, e):
        log.err(e)

class HuxiuStorePipline(object):
    
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', db='mydb',
                user='root', passwd=os.environ.get('MYSQL_PASSWORD',
                cursorclass=MySQLdb.cursors.DictCursor,
                charset='utf8', use_unicode=True)
    
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert,
                item)
        query.addErrback(self.handler_error)
        return item

    def _conditional_insert(self, tx, item):
        tx.execute("""select * from huxiu where title = %s and author = %s and 
                    time = %s """, (item['title'],item['author'],item['time']))
        result = tx.fetchone()
        if result:
            logging.DEBUG("Item already stored in db: %s" % item)
        else:
            tx.execute("""
                 insert into huxiu(title, author, author_url, time, content)
                 values(%s,%s,%s,%s,%s)
                 """, (item['title'],item['author'],item['author_url'],item['time'],item['content']))
            logging.info("Item stored in db:%s" % item)

    def handler_error(self, e):
        logging.error(e)

