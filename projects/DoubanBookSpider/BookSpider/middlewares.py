# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication

import random
import redis

# Start your middleware class
class ProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        # Set the location of the proxy
        current_proxy = self.change_proxy(request)

        retry_times = request.meta.get('retry_times', 0)
        if (retry_times != 0) and (retry_times % 3 == 0):
            current_proxy = self.change_proxy(request):w

        print "Current proxy: " + str(current_proxy) + " Retry times: %d" % retry_times

        # Use the following lines if your proxy requires authentication
        # proxy_user_pass = "joker528@icloud.com:Joker0528"

        # setup basic authentication for the proxy
        # encoded_user_pass = base64.encodestring(proxy_user_pass)
        # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass


    def change_proxy(self, request):
        r = redis.Redis(host='192.168.199.218', port=6379, db=0)
        #rand_index = random.randint(0, r.llen("Proxy:host")-1)
        #proxy_ip = r.lindex("Proxy:host",rand_index)
        try:
            current_proxy = r.rpoplpush("Proxy:host","Proxy:host")
            request.meta['proxy'] = current_proxy
            return current_proxy
        except Exception, e:
            return ''


class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        #print "**************************" + random.choice(self.agents)
        request.headers.setdefault('User-Agent', random.choice(self.agents))
