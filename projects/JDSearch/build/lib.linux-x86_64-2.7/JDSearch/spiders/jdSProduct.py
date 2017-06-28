from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from JDSearch.items import JdsearchItem

class JdSProduct(RedisSpider):
    name = 'jdSProSpider'
    redis_key = 'jdSearchProduct:start_urls'

    def parse(self, response):
        item = JdsearchItem()
        goods = response.xpath('//*[@class="gl-warp clearfix"]/li[@class="gl-item"]')

        for good in goods:
            url = good.xpath('div/div[@class="p-name p-name-type-2"]/a/@href').extract()
            if len(url) == 1:
                if str(url)[3] == '/':
                    item['name'] = good.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()').extract()
                    item['price'] = good.xpath('div/div[@class="p-price"]/strong/i/text()').extract()
                    item['commitNum'] = good.xpath('div/div[@class="p-commit"]/strong/a/text()').extract()
                    item['link'] = 'https:' + str(url[0])
                    yield item