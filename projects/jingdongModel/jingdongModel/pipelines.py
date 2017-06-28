# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi
import copy

class JingdongmodelPipeline(object):

    @classmethod
    def from_settings(cls,settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],  # 读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=False,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbparams)  # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        return cls(dbpool)  # 相当于dbpool付给了这个类，self中可以得到

    def __init__(self, dbpool):
        self.dbpool = dbpool

    def process_item(self, item, spider):

        asynItem=copy.deepcopy(item)
        query = self.dbpool.runInteraction(self._conditional_insert, asynItem)  # 调用插入的方法
        query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item

    def _conditional_insert(self,tx,item):
        if item['nothing']==1:
            sql = "insert into jdmodelinfo(title,location,violationTimes,link) values(%s,%s,%s,%s)"
            params = (item['title'],item['location'],item['violationTimes'],item['link'])
        else:
            sql = "insert into jdmodelinfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            params = (item['title'], item['location'],item['link'],item['shopAveScore'], item['shopAveScore_comRate'],
                      item['goodsContent'], item['goodsContent_comRate'], item['serveAttitude'],
                      item['serveAttitude_comRate'],
                      item['transSpeed'], item['transSpeed_comRate'], item['goodsDescribe'],
                      item['goodsDescribe_comRate'],
                      item['backGoods'], item['backGoods_comRate'], item['aftersalesDealTIme'],
                      item['aftersalesDealTIme_comRate'],
                      item['dealDispute'], item['dealDispute_comRate'], item['backRepair'], item['backRepair_comRate'],
                      item['violationTimes'])
        tx.execute(sql, params)

    def _handle_error(self, failue, item, spider):
        print failue
