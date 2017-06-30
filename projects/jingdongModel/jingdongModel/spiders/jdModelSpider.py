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
    r = redis.Redis(host='db2.daocloudinternal.io', port=60222, db=0, password='KZ80pnCx')
    #r.delete('jdModelIn:start_urls')

    def parse(self, response):
        self.r.lpush('jdModelIn:start_urls', response.url)
