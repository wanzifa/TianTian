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
reload(sys)
sys.setdefaultencoding('utf8')

class RdspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class SQLStorePipeline(object):

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
                select * from guoke  where title = %s and author = %s
        """,(item['title'], item['author']))
        result = tx.fetchone()
        if result:
            log.msg("Item already stored in db: %s" % item,
                    level=log.DEBUG)
        else:
            tx.execute("insert into guoke values(%s,%s)",  (item['title'],item['author']))
            log.msg("Item stored in db: %s" % item, level=log.DEBUG)

    def handler_error(self, e):
        log.err(e)

