# -*- coding: utf-8 -*-

import redis
import subprocess
r = redis.Redis(host='db2.daocloudinternal.io', port=60222, db=0, password='KZ80pnCx')

#Validating
length = r.llen("TempProxy:host")
print "----- %d Proxies -----" % length
i = 0
while (i < length):
    print "      No.%d Proxy      " % (i+1)
    subprocess.call(["scrapy", "crawl", "ProxyTestSpider","--nolog"])
    i += 1
