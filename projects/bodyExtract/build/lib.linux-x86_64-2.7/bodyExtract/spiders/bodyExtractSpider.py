# -*- coding: utf-8 -*-
import scrapy
import os
import os.path
import redis

class bodyExtractSpider(scrapy.Spider):
    name = 'bodyExtract'
    #遍历源文件夹所有文件 拼接成起始地址
    dir = '/home/imisswonder/zw/'
    urls = []
    for filenames in os.listdir(dir):
        urls.append('file:///home/imisswonder/zw/'+filenames)
        #urls.append('file:///home/miemielinux/linuxSoftCup/offiData/test/' + filenames)
    start_urls = urls
    r = redis.Redis(host='192.168.199.218', port=6379, db=0)
    r.delete('bodyExtract:start_urls')

    def parse(self, response):
        self.r.lpush('bodyExtract:start_urls', response.url)

