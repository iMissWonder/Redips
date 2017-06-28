# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongmodelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()#店铺名
    location = scrapy.Field()#所在地
    link = scrapy.Field()
    nothing = scrapy.Field()

    shopAveScore = scrapy.Field()#店铺综合评分
    shopAveScore_comRate = scrapy.Field()#店铺综合评分-与同行平均水平

    #180天内店铺动态评分
    goodsContent = scrapy.Field()#商品满意度
    goodsContent_comRate = scrapy.Field()#商品满意度-与同行平均水平
    serveAttitude = scrapy.Field()#服务满意度
    serveAttitude_comRate = scrapy.Field()#服务满意度-与同行平均水平
    transSpeed = scrapy.Field()#物流速度满意度
    transSpeed_comRate =scrapy.Field()#物流速度满意度-与同行平均水平
    goodsDescribe = scrapy.Field()#商品描述满意度
    goodsDescribe_comRate = scrapy.Field()
    backGoods = scrapy.Field()#退换货处理满意度
    backGoods_comRate = scrapy.Field()
    hasBackGoods = scrapy.Field()

    #90天内平台监控店铺服务
    aftersalesDealTIme = scrapy.Field()#售后处理时长
    aftersalesDealTIme_comRate = scrapy.Field()
    dealDispute = scrapy.Field()#交易纠纷率
    dealDispute_comRate = scrapy.Field()
    backRepair = scrapy.Field()#退换货返修率
    backRepair_comRate = scrapy.Field()

    violationTimes = scrapy.Field()#店铺违法违规信息次数
    pass
