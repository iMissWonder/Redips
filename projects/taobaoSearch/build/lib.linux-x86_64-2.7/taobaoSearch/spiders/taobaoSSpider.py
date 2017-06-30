# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from selenium import webdriver #动态
import time
import redis

class TaoBaoSearchSpider(scrapy.Spider):
    name = 'taobaoSSpider'
    start_urls=['https://s.taobao.com/search?q=iPhone&s=0']
    r = redis.Redis(host='db2.daocloudinternal.io', port=60222, db=0, password='KZ80pnCx')
    #r.delete('taobaoSearchProduct:start_urls')

    def parse(self, response):
        i = 0
        lastSearchUrls = []
        while i < 5:
            lastSearchUrls.append( 'https://s.taobao.com/search?q='+ self.settings.get('TARGET') + "&s=" + str(i * 44))
            i = i + 1
        for lastSearchUrl in lastSearchUrls:
            request = Request(lastSearchUrl, callback=self.parse_list)
            yield request

    def parse_list(self,response):
        driver = webdriver.PhantomJS()
        driver.get(response.url)
        time.sleep(1)
        selector = Selector(text=driver.page_source)
        driver.close()

        tempLinks = selector.xpath(
            '//div[@class="item J_MouserOnverReq  "]/div/div/div[@class="pic"]/a/@href').extract()

        for tempLink in tempLinks:
            if tempLink[2] == "i":
                tempLink = "https:" + tempLink
                self.r.lpush('taobaoSearchProduct:start_urls',tempLink)
