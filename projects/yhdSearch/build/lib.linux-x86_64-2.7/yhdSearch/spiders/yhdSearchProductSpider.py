# -*- coding: utf-8 -*-

from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from yhdSearch.items import YhdsearchItem

class yhdSearchProductSpider(RedisSpider):
    name = 'yhdSPSpider'
    redis_key = 'yhdSearchProduct:start_urls'

    def parse(self, response):
        item = YhdsearchItem()  # 创建YhdItem对象
        # 通过xpath解析html
        item['title'] = response.xpath('//h1[@id="productMainName"]/text()').extract()
        price_str = response.xpath('//a[@class="ico_sina"]/@href').extract()[0]
        item['price'] = price_str
        item['link'] = response.url
        pmld = response.url.split('/')[-1]
        price_url = 'http://gps.yhd.com/restful/detail?mcsite=1&provinceId=12&pmId=' + pmld
        item['category'] = response.xpath(
            '//div[@class="crumb clearfix"]/a[contains(@onclick,"detail_BreadcrumbNav_cat")]/text()').extract()
        item['product_id'] = response.xpath('//p[@id="pro_code"]/text()').extract()
        item['img_link'] = response.xpath('//img[@id="J_prodImg"]/@src').extract()[0]
        request = Request(price_url, callback=self.parse_price)  # 商品的价格需要异步获取,通过商品ID获取价格
        request.meta['item'] = item
        yield request

    def parse_price(self, response):
        item = response.meta['item']
        item['price'] = response.body
        temp = item['price'].split(',')[12]
        item['currentPrice'] = temp.split(':')[1]
        return item