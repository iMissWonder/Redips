# - * - coding: utf-8 - * -

import redis
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider

class BookURLSpider(RedisSpider):
    name = 'BookURLSpider'
    redis_key = "BookURLSpider:start_urls"
    r = redis.Redis(host='192.168.199.218', port=6379, db=0)
    r.lpush('BookURLSpider:start_urls','https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4')

    def parse(self, response):
        selector = Selector(response)
        #self.r.delete('BookContentSpider:start_urls')
        book_urls = selector.xpath("//div[@class='info']/h2/a/@href").extract()

        for book in book_urls:
            self.r.lpush('BookContentSpider:start_urls',book)

        next_link = selector.xpath("//span[@class='next']/a/@href").extract()
        if next_link:
            next_link = "https://book.douban.com" + next_link[0]
            yield Request(next_link,callback=self.parse)
