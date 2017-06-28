# !/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'fhy'
import json
from scrapy import  signals
class ReplaceRequestToPhantomjsProxy(object):

    @classmethod
    def from_crawler(cls, crawler):
        midd = cls(crawler.settings)
        # crawler.signals.connect(midd.close_spider, signals.spider_closed)
        crawler.signals.connect(midd.open_spider, signals.spider_opened)
        return midd

    def __init__(self, settings):
        self.default_options = {
            'url':" ",
            'callback': None,
            'method': 'GET',
            'headers': None,
            'body': None,
            'cookies': None,
            'meta': None,
            'encoding': 'utf-8',
            'priority': 0,
            'dont_filter': False,
            'errback': None
        }
        self.js_execute_proxy_default = settings.get('JS_EXECUTE_PROXY')

    def open_spider(self, spider):
        # self.js_execute_proxy = getattr(spider, 'js_execute_proxy', self.js_execute_proxy_default)

        self.js_execute_proxy = "http://127.0.0.1:8006"

    def close_spider(self, spider):
        self.conn.close()

    @staticmethod
    def parse_option(default_options, url, request, **kwargs):
        fetch = default_options
        # for x in ['url', 'method', 'headers', 'body', 'cookies', 'meta',
        #           'encoding', 'priority', 'dont_filter', 'callback', 'errback']:
        #     fetch[x] = request.get(x, default_options[x])
        fetch['method']=request.method
        fetch['body']=request._get_body()
        fetch['encoding']=request._encoding
        fetch['priority']=request.priority
        fetch['dont_filter']=request.dont_filter
        fetch['callback']=request.callback
        fetch['errback']=request.errback
        fetch['meta'] = request.meta
        fetch['cookies'] = request.cookies
        fetch['headers'] = request.headers
        fetch['url'] = url
        js_script = kwargs.get('js_script')
        if js_script:
            fetch['js_script'] = js_script
            fetch['js_run_at'] = kwargs.get('js_run_at', 'document-end')
        fetch['load_images'] = kwargs.get('load_images', False)
        return fetch

    def process_request(self, request, spider):
        # print("haha")
        # print(request.url)
        # if request.url=="http://weibo.com/" or request.url=="https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=http%3A%2F%2Fweibo.com%2F&domain=.weibo.com&ua=php-sso_sdk_client-0.6.14&_rand=1460024847.6304":
        #     return
        # if request.url=="http://weibo.com/" or request.url.split('?')[0]=="https://passport.weibo.com/visitor/visitor" :
        #     return
        if request.url == self.js_execute_proxy:
            return
        fetch = self.parse_option(
            default_options=self.default_options,
            url=request.url,
            request=request
        )
        request._set_url(self.js_execute_proxy)
        request.method = 'POST'
        request.headers["Content-Type"] = "application/x-www-form-urlencoded"
        # print("zjk")
        # print(request.url)
        # request._set_body(json.dumps({'url': request.url}))
        request._set_body(json.dumps(fetch))
        # print request.headers
        print 'asd'
        print(fetch['cookies'])
        print(fetch['url'])
        # print request.body
        # print '———————————'
        return  request
