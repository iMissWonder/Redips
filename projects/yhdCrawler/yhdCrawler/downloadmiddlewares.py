# -*- coding: utf-8 -*-

__author__ = 'bitfeng'
# Define your downloadmiddlware here

import random
import logging


class RandomUserAgent(object):
    userAgents = {
        'PC': [
            # safari 5.1 – MAC
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            # safari 5.1 – Windows
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            # IE 9.0
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
            # IE 8.0
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
            # IE 7.0
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
            # IE 6.0
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
            # Firefox 4.0.1 – MAC
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            # Firefox 4.0.1 – Windows
            'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            # Opera 11.11 – MAC
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            # Opera 11.11 – Windows
            'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
            # Chrome 17.0 – MAC
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            # 傲游（Maxthon）
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
            # 腾讯TT
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
            # 世界之窗（The World） 2.x
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            # 世界之窗（The World） 3.x
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
            # 搜狗浏览器 1.x
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
            # 360浏览器
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
            # Avant
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
            # Green Browser
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        ],

        'mobile': [
            # 移动设备端：
            # safari iOS 4.33 – iPhone
            'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
            # safari iOS 4.33 – iPod Touch
            'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
            # safari iOS 4.33 – iPad
            'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
            # Android N1
            'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            # Android QQ浏览器 For android
            'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            # Android Opera Mobile
            'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
            # Android Pad Moto Xoom
            'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
            # BlackBerry
            'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
            # WebOS HP Touchpad
            'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0',
            # Nokia N97
            'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124',
            # Windows Phone Mango
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
            # UC无
            'UCWEB7.0.2.37/28/999',
            # UC标准
            'NOKIA5700/ UCWEB7.0.2.37/28/999',
            # UCOpenwave
            'Openwave/ UCWEB7.0.2.37/28/999',
            # UC Opera
            'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',
        ]
    }

    def process_request(self, request, spider):
        user_agent = random.choice(self.userAgents['PC'])
        if user_agent:
            request.headers.setdefault(b'User-Agent', user_agent)


class LogHttpErrorStatusUrl(object):

    def process_response(self, request, response, spider):
        if response.status < 200 or response.status > 300:
            logging.log(logging.INFO, spider.name+':'+str(response.status)+' | '+response.url)
        return response


class LogRequestResponseUrl(object):

    def process_response(self, request, response, spider):
        logging.log(logging.INFO, 'Response:'+response.url)
        return response

    def process_request(self, request, spider):
        logging.log(logging.INFO, 'Request:'+request.url)
        return