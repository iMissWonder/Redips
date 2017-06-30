# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
import redis

class YhdSpider(scrapy.Spider):
    name = 'yhdSpider'
    start_urls = ['http://www.yhd.com/marketing/allproduct.html']
    r = redis.Redis(host='db2.daocloudinternal.io', port=60222, db=0, password='KZ80pnCx')
    #r.delete('yhdProduct:start_urls')

    def parse(self, response):
        urls = response.xpath('//dl[@class="fore"]/dt/a/@href').extract()
        for url in urls:
            if url!="kids.yhd.com/" \
                    and url!="http://yhd.aicai.com/" \
                    and url!="http://search.yhd.com/c0-0/k%E9%B2%9C%E8%8A%B1%E9%80%9F%E9%80%92/"\
                    and url!="http://search.yhd.com/c0-0/k%E6%B8%85%E6%B4%81%E5%B7%A5%E5%85%B7-%E4%B8%80%E6%AC%A1%E6%80%A7%E7%94%A8%E5%93%81/":
                # url="http:"+url+"#page=1&sort=1"
                url="http:"+url
                request = Request(url, callback=self.parse_page)
                yield request

    def parse_page(self,response):
        i = 1
        next_page_urls=[]
        while i<=50:
            #next_page_urls.append(response.url+"#page="+str(i)+"&sort=1")
            next_page_urls.append(response.url + "b/a-s1-v4-p"+str(i)+"-price-d0-f0-m1-rt0-pid-mid0-k/")
            i = i + 1
        for next_page_url in  next_page_urls:
            request = Request(next_page_url, callback=self.parse_list)
            yield request

    def parse_list(self, response):
        product_urls = response.xpath('//div[@class="itemBox"]/p[@class="proName clearfix"]/a/@href').extract()
        for product_url in product_urls:
            product_url = 'http:'+ product_url
            if product_url.split(':')[0]=="http": #去除莫名的tracker项
                self.r.lpush('yhdProduct:start_urls',product_url)
