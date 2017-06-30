# -*- coding: utf-8 -*-
import scrapy
import redis
from scrapy.selector import Selector
import urllib
import socket

class ProxySpider(scrapy.Spider):
    name = "ProxySpider"
    allowed_domains = ["www.xicidaili.com"]
    start_urls = ['http://www.xicidaili.com/nn']

    def parse(self, response):
        selector = Selector(response)
        proxy_ip_list = selector.xpath('//td[2]/text()').extract()
        proxy_port_list = selector.xpath('//td[3]/text()').extract()

        r = redis.Redis(host='db2.daocloudinternal.io', port=60222, db=0, password='KZ80pnCx')
        r.delete('TempProxy:host')
        r.delete('Proxy:host')
        ip_test_url = 'http://ip.chinaz.com/getip.aspx'
        #socket.setdefaulttimeout(3)
        for ip, port in zip(proxy_ip_list, proxy_port_list):
            proxy_host = "http://" + ip + ":" + port
            r.lpush('TempProxy:host', proxy_host)

    '''
    try:
        proxy_host = "http://" + ip + ":" + port
        proxy_temp = {"http": proxy_host}
        res = urllib.urlopen(ip_test_url, proxies=proxy_temp).read()
        print proxy_host
        r.lpush('Proxy:host', proxy_host)
    except Exception, e:
        continue
    '''
