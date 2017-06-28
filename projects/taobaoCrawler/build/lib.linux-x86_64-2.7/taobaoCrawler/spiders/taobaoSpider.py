# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from selenium import webdriver #动态
import time
import redis

class TaoBaoSpider(scrapy.Spider):
    name='taobaoSpider'
    start_urls=["https://www.taobao.com/"]
    r = redis.Redis(host='192.168.199.218', port=6379, db=0)
    #r.delete('taobaoProduct:start_urls')

    def parse(self, response):
        searchItems=response.xpath('//li[@class="J_Cat a-all"]/span/a/text()').extract()
        for searchItem in searchItems:
            searchUrl="https://s.taobao.com/search?q="+searchItem
            request = Request(searchUrl, callback=self.parse_pageExtend)
            yield request

    def parse_pageExtend(self,response):
        i = 0
        lastSearchUrls=[]
        while i<5:
            lastSearchUrls.append(response.url+"&s="+str(i*44))
            i=i+1
        for lastSearchUrl in lastSearchUrls:
            request=Request(lastSearchUrl,callback=self.parse_list)
            yield request

    def parse_list(self,response):#进入动态 最终搜索页
        driver = webdriver.PhantomJS()
        driver.get(response.url)
        time.sleep(1)
        selector = Selector(text=driver.page_source)
        driver.close()

        tempLinks=selector.xpath('//div[@class="item J_MouserOnverReq  "]/div/div/div[@class="pic"]/a/@href').extract()
        for tempLink in tempLinks:
            if tempLink[2]=="i":
                tempLink="https:"+tempLink
                self.r.lpush('taobaoProduct:start_urls',tempLink)


