# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from taobaoSearch.items import TaobaosearchItem
from selenium import webdriver

class YhdProductSpider(RedisSpider):
    name = 'taobaoSProSpider'
    redis_key = 'taobaoSearchProduct:start_urls'

    def parse(self,response):
        item = TaobaosearchItem()
        item['link'] = response.url

        driver = webdriver.PhantomJS()
        driver.get(response.url)
        #time.sleep(1)
        selector = Selector(text=driver.page_source)
        driver.close()

        item['title'] = selector.xpath('//h3[@class="tb-main-title"]/@data-title').extract()
        item['price'] = selector.xpath('//strong[@id="J_StrPrice"]/em[@class="tb-rmb-num"]/text()').extract()
        item['taobaoPrice'] = selector.xpath('//strong[@class="tb-promo-price"]/em[@id="J_PromoPriceNum"]/text()').extract()
        #item['location'] = selector.xpath('//span[@id="J_WlAreaInfo"]/span[@id="J-From"]/text()').extract()
        item['shop'] = selector.xpath('//strong/a/@title').extract()
        item['commentsNum'] = selector.xpath('//strong[@id="J_RateCounter"]/text()').extract()
        item['dealDoneNum'] = selector.xpath('//strong[@id="J_SellCounter"]/text()').extract()
        #item['lastcmtTIme'] = selector.xpath('//li[@class="J_KgRate_ReviewItem kg-rate-ct-review-item"]/div[@class="review-details"]/div[@class="tb-rev-item "]/div[@class="tb-r-act-bar"]/div/span/text()').extract()
        yield item



