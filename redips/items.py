# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RedipsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    shop = scrapy.Field()
    price = scrapy.Field()
    trading = scrapy.Field()
    review = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
