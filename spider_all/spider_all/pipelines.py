#coding: utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import datetime
import MySQLdb.cursors
import sys
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
                logging.debug("Item already stored in db: %s" % item['name'])
            else:
                tx.execute("""
                insert into guoke(title, author, author_url, time, content, category)
                values(%s,%s,%s,%s,%s,%s) 
                """, (item['title'],item['author'],item['author_url'], item['time'], item['content'], item['category']))
                logging.info("Item stored in db: %s" % item)
        elif item['name'] == 'huxiu':
            tx.execute(""" 
                   select * from huxiu where author=%s and title=%s 
            """,(item['author'],item['title']))
            result = tx.fetchone()
            if result:
                logging.debug("Item already stored in db: %s" % item['name'])
            else:
                tx.execute("""
                insert into huxiu(title, author, author_url, time, content, category)
                values(%s,%s,%s,%s,%s,%s) 
                """, (item['title'],item['author'],item['author_url'], item['time'], item['content'], item['category']))
                logging.info("Item stored in db: %s" % item)
        elif item['name'] == 'douban':
           tx.execute(""" 
                  select * from douban where author=%s and title=%s 
           """,(item['author'],item['title']))
           result = tx.fetchone()
           if result:
               logging.debug("Item already stored in db: %s" % item['name'])
           else:
               tx.execute("""
               insert into douban(title, author, author_url, time, content, book_name,book_url)
               values(%s,%s,%s,%s,%s,%s,%s) 
               """, (item['title'],item['author'],item['author_url'], item['time'], item['content'], item['book_name'],item['book_url']))
               logging.info("Item stored in db: %s" % item)
        elif item['name'] == 'zhihu':
           tx.execute(""" 
                  select * from zhihu where author=%s and title=%s 
           """,(item['author'],item['title']))
           result = tx.fetchone()
           if result:
               logging.debug("Item already stored in db: %s" % item['name'])
           else:
               tx.execute("""
               insert into zhihu(title, author, author_url, time, content, category)
               values(%s,%s,%s,%s,%s,%s) 
               """, (item['title'],item['author'],item['author_url'], item['time'], item['content'], item['category']))
               logging.info("Item stored in db: %s" % item)
   
>>>>>>> 534ad2a75abaadc4ef88c61708245d352e5488db
    def handler_error(self, e):
        logging.error(e)


