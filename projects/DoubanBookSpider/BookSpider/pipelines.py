# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi
import copy

class DoubanBookPipeline(object):
    @classmethod
    def from_settings(cls, settings):
        '''1、@classmethod声明一个类方法，而对于平常我们见到的则叫做实例方法。 
           2、类方法的第一个参数cls（class的缩写，指这个类本身），而实例方法的第一个参数是self，表示该类的一个实例
           3、可以通过类来调用，就像C.f()，相当于java中的静态方法'''
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

    # pipeline默认调用
    def process_item(self, item, spider):
        asynItem=copy.deepcopy(item)
        query = self.dbpool.runInteraction(self._conditional_insert, asynItem)  # 调用插入的方法
        query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item

    def _conditional_insert(self, tx, item):
        # tpisbn = ""
        # for ids in item['isbn13']:
        #     if tpisbn == "":
        #         tpisbn = ids + ""
        #     else:
        #         tpisbn = tpisbn + ids + ""
        # tppublisher = ""
        # for ids in item['publisher']:
        #     if tppublisher == "":
        #         tppublisher = ids + ""
        #     else:
        #         tppublisher = tppublisher + ids + ""
        # tppudate = ""
        # for ids in item['pubdate']:
        #     if tppudate == "":
        #         tppudate = ids + ""
        #     else:
        #         tppudate = tppudate + ids + ""
        # tpprice = ""
        # for ids in item['price']:
        #     if tpprice == "":
        #         tpprice = ids + ""
        #     else:
        #         tpprice = tpprice + ids + ""
        tpreview_id = ""
        for ids in item['review_id']:
            if tpreview_id == "":
                tpreview_id = ids + " "
            else:
                tpreview_id = tpreview_id + ids + " "

        tpshort_review_name = ""
        for ids in item['review_name']:
            if tpshort_review_name == "":
                tpshort_review_name = ids + " "
            else:
                tpshort_review_name = tpshort_review_name + ids + " "

        tpshort_review_link = ""
        for ids in item['review_link']:
            if tpshort_review_link == "":
                tpshort_review_link = ids + " "
            else:
                tpshort_review_link = tpshort_review_link + ids + " "

        tpshort_review_title = ""
        for ids in item['review_title']:
            if tpshort_review_title == "":
                tpshort_review_title = ids + " "
            else:
                tpshort_review_title = tpshort_review_title + ids + " "

        tpshort_review_id = ""
        for ids in item['short_review_id']:
            if tpshort_review_id == "":
                tpshort_review_id = ids + " "
            else:
                tpshort_review_id = tpshort_review_id + ids + " "

        tpshort_review_name = ""
        for ids in item['short_review_name']:
            if tpshort_review_name == "":
                tpshort_review_name = ids + " "
            else:
                tpshort_review_name = tpshort_review_name + ids + " "

        tpshort_review_content = ""
        for ids in item['short_review_content']:
            if tpshort_review_content == "":
                tpshort_review_content = ids + ""
            else:
                tpshort_review_content = tpshort_review_content + ids + ""

        tpimage = ""
        for ids in item['image']:
            if tpimage == "":
                tpimage = ids + ""
            else:
                tpimage = tpimage + ids + ""

        tpcatalog = ""
        for ids in item['catalog']:
            if tpcatalog == "":
                tpcatalog = ids + ""
            else:
                tpcatalog = tpcatalog + ids + ""

        tptitle = ""
        for ids in item['title']:
            if tptitle == "":
                tptitle = ids + ""
            else:
                tptitle = tptitle + ids + ""

        tpsum = ""
        for ids in item['summary']:
            if tpsum == "":
                tpsum = ids + ""
            else:
                tpsum = tpsum + ids + ""



        # sql = "insert into doubaninfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # params = (item['book_id'], item['title'], item['author'], tpisbn,
        #           tppublisher,tppudate,tpprice,item['pages'],
        #           item['translator'],item['summary'],item['catalog'],item['lookcount'],
        #           item['image'], item['tryread'], item['short_review_content'], item['short_review_name'],
        #           item['short_review_id'], item['review_title'], item['review_link'], item['review_name'],
        #           item['review_id'])
        sql = "insert into doubaninfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (item['book_id'],tptitle,item['author'],item['isbn13'],item['publisher'],item['pubdate'],item['price'],item['pages'],
                  item['translator'],tpsum,tpcatalog,item['lookcount'],tpimage,item['tryread'],tpshort_review_content,
                  tpshort_review_name,tpshort_review_id,tpshort_review_title,tpshort_review_link,tpshort_review_name,tpreview_id)
        tx.execute(sql, params)

    def _handle_error(self, failue, item, spider):
        print failue
