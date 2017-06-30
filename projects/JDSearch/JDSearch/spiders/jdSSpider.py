import scrapy
import redis

class JdSSpider(scrapy.Spider):
    name = 'jdSSpider'
    start_urls = ["https://search.jd.com/Search?keyword=iPhone&enc=utf-8&wq=iPhone"]
    r = redis.Redis(host='db2.daocloudinternal.io', port=60222, db=0, password='KZ80pnCx')
    #r.delete('jdSearchProduct:start_urls')

    def parse(self, response):
        i = 0
        lastSearchUrls = []
        while i < 50:
            lastSearchUrls.append('https://search.jd.com/Search?keyword='+ self.settings.get('TARGET')
                                  +'&enc=utf-8&wq='+ self.settings.get('TARGET') + "&page=" + str(i * 2 + 1))
            i = i + 1
        for lastSearchUrl in lastSearchUrls:
             self.r.lpush('jdSearchProduct:start_urls',lastSearchUrl)
