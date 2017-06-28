# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from  jingdongModel.items import JingdongmodelItem

class JdModelSpiderIn(RedisSpider):
    name = 'jdmSpiderIn'
    redis_key = 'jdModelIn:start_urls'

    def parse(self, response):
        item = JingdongmodelItem()

        item['title'] = response.xpath('//div[@class="jLogo"]/em/text()').extract()
        item['location'] = response.xpath('//div[@class="j-shop-info"]/p[3]/span[2]/text()').extract()
        item['link'] = response.url
        item['violationTimes'] = response.xpath('//span[@class="f18 c005aa0 bold"]/a/text()').extract()

        score = response.xpath('//div[@class="item-180 f14"]/span[2]/text()').extract()  # 分值的span类名可能不一样
        comRate = response.xpath('//span[@class="percent"]/text()').extract()

        if comRate[0] == '%':
            item['nothing'] = 1
        else:
            item['nothing'] = 0
            item['shopAveScore'] = response.xpath('//p[@class="total-score-num"]/span/text()').extract()
            item['shopAveScore_comRate'] = comRate[0]
            judge = response.xpath('//p[@class="score-des"]/span[1]/text()').extract()
            if len(comRate) >= 2:
                item['goodsContent'] = score[0]
                item['goodsContent_comRate'] = comRate[1]
            else:
                item['goodsContent'] = '暂无'
                item['goodsContent_comRate'] = '暂无'
            if len(comRate) >= 3:
                item['serveAttitude'] = score[1]
                item['serveAttitude_comRate'] = comRate[2]
            else:
                item['serveAttitude'] = '暂无'
                item['serveAttitude_comRate'] = '暂无'
            if len(comRate) >= 4:
                item['transSpeed'] = score[2]
                item['transSpeed_comRate'] = comRate[3]
            else:
                item['transSpeed'] = '暂无'
                item['transSpeed_comRate'] = '暂无'
            if len(comRate) >= 5:
                item['goodsDescribe'] = score[3]
                item['goodsDescribe_comRate'] = comRate[4]
            else:
                item['goodsDescribe'] = '暂无'
                item['goodsDescribe_comRate'] = '暂无'
            if len(comRate) >= 6:
                item['backGoods'] = score[4]
                item['backGoods_comRate'] = comRate[5]
            else:
                item['backGoods'] = '暂无'
                item['backGoods_comRate'] = '暂无'

            selfValue = response.xpath('//span[@class="f16 value"]/text()').extract()
            item['aftersalesDealTIme'] = selfValue[0]
            item['aftersalesDealTIme_comRate'] = selfValue[1]
            item['dealDispute'] = selfValue[2]
            item['dealDispute_comRate'] = selfValue[3]
            item['backRepair'] = selfValue[4]
            item['backRepair_comRate'] = selfValue[5]
        yield item