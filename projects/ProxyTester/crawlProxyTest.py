# -*- coding: utf-8 -*-

from scrapy_redis import get_redis
import subprocess
r = get_redis()

#Validating
length = r.llen("TempProxy:host")
print "----- %d Proxies -----" % length
i = 0
while (i < length):
    print "      No.%d Proxy      " % (i+1)
    subprocess.call(["scrapy", "crawl", "ProxyTestSpider","--nolog"])
    i += 1
