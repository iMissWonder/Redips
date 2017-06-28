# -*- coding: utf-8 -*-
import codecs
import urllib2
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider
from bodyExtract.items import BodyextractItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class bodyExtractInSpider(RedisSpider):
    name = 'bodyExtractIn'
    redis_key = 'bodyExtract:start_urls'

    def parse(self, response):
        item = BodyextractItem()
        filename = response.url.split('/')[-1]

        if filename[0]=='b':#新浪
            fileObject = codecs.open('/home/imisswonder/outputExtractData/' + filename, 'w','utf-8')
            fileObject.write(''.join(response.xpath('//div[@id = "sina_keyword_ad_area2"]//text()').extract()))
            fileObject.close()
            item['content'] = response.xpath('//div[@id = "sina_keyword_ad_area2"]//text()').extract()

        elif filename[0]=='B' or filename[0] =='C':#网易(2个bgk编码)
            handle = urllib2.urlopen(response.url)  # 得到句柄
            html = handle.read()  # 得到html源代码
            html = unicode(html)  # 转换为unicode (utf8编码)
            selector = Selector(text=html)  # 赋值选择器
            fileObject = codecs.open('/home/imisswonder/outputExtractData/' + filename, 'w','utf-8')
            fileObject.write(''.join(selector.xpath('//div[@id ="endText"][1]//text()').extract()))
            fileObject.close()
            item['content'] = selector.xpath('//div[@id ="endText"][1]//text()').extract()
            handle.close()

        elif filename[0]=='q':#腾讯（全部gb2312编码）
            handle = urllib2.urlopen(response.url)  # 得到句柄
            html = handle.read()  # 得到html源代码
            html = unicode(html)  # 转换为unicode (utf8编码)
            selector = Selector(text=html)  # 赋值选择器
            fileObject = codecs.open('/home/imisswonder/outputExtractData/' + filename, 'w','utf-8')
            fileObject.write(''.join(selector.xpath('//div[@id = "Cnt-Main-Article-QQ"]//text()').extract()).encode('utf-8'))
            fileObject.close()
            item['content'] = selector.xpath('//div[@id = "Cnt-Main-Article-QQ"]//text()').extract()
            handle.close()
        yield item
