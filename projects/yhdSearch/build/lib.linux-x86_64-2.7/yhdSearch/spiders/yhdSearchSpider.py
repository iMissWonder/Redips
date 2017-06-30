# -*- coding: utf-8 -*-
from scrapy.http import Request
import scrapy.crawler
import redis

class YhdSearchSpider(scrapy.Spider):
    name = 'yhdSSpider'
    start_urls=['http://search.yhd.com/c0-0-0/b/a-s1-v4-p3-price-d0-f0-m1-rt0-pid-mid0-kiphone']
    r = redis.Redis(host='db2.daocloudinternal.io', port=60222, db=0, password='KZ80pnCx')
    #r.delete('yhdSearchProduct:start_urls')

    def parse(self, response):
        i = 0
        next_page_urls = []
        while i <= 50:
            next_page_urls.append('http://search.yhd.com/c0-0-0/b/a-s1-v4-p'+str(i)+'-price-d0-f0-m1-rt0-pid-mid0-k'+self.settings.get('TARGET'))
            i = i + 1
        for next_page_url in next_page_urls:
            request = Request(next_page_url, callback=self.parse_list)
            yield request

    def parse_list(self,response):
        producturls = response.xpath('//div[@class="itemBox"]/p[@class="proName clearfix"]/a/@href').extract()
        for product_url in producturls:
            product_url = "http:" + product_url
            if product_url.split(':')[0] == "http":  # 去除莫名的tracker项
                self.r.lpush('yhdSearchProduct:start_urls', product_url)
