# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import base64
import redis
from scrapy import signals

CHANGE_PROXY_STATUS_LIST = [502, 404]

class ProxyMiddleware(object):
    r = redis.Redis(host='db2.daocloudinternal.io',port = 60222, db = 0, password='KZ80pnCx')
    proxy_host =  r.rpoplpush("TempProxy:host","Proxy:host")

    def process_request(self, request, spider):
        # Set the location of the proxy
        request.meta['proxy'] = self.proxy_host
        retry_times = request.meta.get('retry_times', 0)
        if retry_times >= 4:
            return
        print "Current proxy: " + request.meta['proxy'] + " Retry times: %d" % retry_times

        # Use the following lines if your proxy requires authentication
        proxy_user_pass = "iMissWonder-SP3: "

        # setup basic authentication for the proxy
        encoded_user_pass = base64.encodestring(proxy_user_pass)
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

    def process_exception(self, request, exception, spider):
        current_proxy = request.meta['proxy']
        try:
            self.del_proxy(current_proxy)
        except ValueError:
            pass
        #return request

    def del_proxy(self, current_proxy):
        print ('Remove proxy: %s, %d proxies left' % (
            current_proxy, self.r.llen("Proxy:host")-1))
        self.r.lrem("Proxy:host", 0, current_proxy)
        print "Successfully removed :" + current_proxy

    '''
    def change_proxy(self, request):
        proxy_host =  self.r.rpoplpush("Proxy:host","Proxy:host")
        request.meta['proxy'] = proxy_host
        return proxy_host
        # Change proxy here
        # Then check number of retries on the request
        # and decide if you want to give it another chance.
        # If not - return None else
    def process_exception(self, request, exception, spider):
        return_request = self.change_proxy(request)
        if return_request:
            return return_request

    def process_response(self, request, response, spider):
        if response.status in CHANGE_PROXY_STATUS_LIST:
            return_request = self.change_proxy(request)
            if return_request:
                return return_request
        return response

    '''
