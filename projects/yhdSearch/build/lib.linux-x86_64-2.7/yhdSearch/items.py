# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YhdsearchItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()  # 商品名称
    price = scrapy.Field()  # 商品价格
    currentPrice = scrapy.Field()
    link = scrapy.Field()  # 商品链接
    category = scrapy.Field()  # 商品分类
    product_id = scrapy.Field()  # 产品ID
    img_link = scrapy.Field()  # 图片链接
    pass
