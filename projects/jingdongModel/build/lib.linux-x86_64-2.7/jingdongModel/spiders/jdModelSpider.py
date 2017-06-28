import scrapy
import os
import redis

class jdModelSpider(scrapy.Spider):
    name = 'jdmSpider'
    dir = "/home/imisswonder/jd"
    urls = []
    for filenames in os.listdir(dir):
        urls.append('file:///home/imisswonder/jd/' + filenames)
    start_urls = urls
    r = redis.Redis(host='192.168.199.218', port=6379, db=0)
    #r.delete('jdModelIn:start_urls')

    def parse(self, response):
        self.r.lpush('jdModelIn:start_urls', response.url)
