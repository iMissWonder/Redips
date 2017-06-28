import time

from scrapy.dupefilters import BaseDupeFilter
from scrapy.utils.request import request_fingerprint
from . import bloomfilter

from . import connection


class RFPDupeFilter(BaseDupeFilter):

    def __init__(self, server, key):

        self.server = server
        self.key = key
        self.bloomfilters=bloomfilter.BloomFilter(connection=self.server,
                        bitvector_key=self.key,
                        n=1024*8,
                        k=4)
        self.count=0

    @classmethod
    def from_settings(cls, settings):
        server = connection.from_settings(settings)
        # key = "dupefilter:%s" % int(time.time())
        key = "dupefilterbloom:%s" % int(time.time())
        return cls(server, key)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    # def request_seen(self, request):
    #     fp = request_fingerprint(request)
    #     added = self.server.sadd(self.key, fp)
    #     if not added:
    #         self.count=self.count+1
    #         print("chongfu")
    #         print(self.count)
    #     return not added

    def request_seen(self, request):
        fp = request_fingerprint(request)
        if self.bloomfilters.__contains__(fp):
            self.count=self.count+1
            #print("chongfu")
            #print(self.count)
            return  True
        else:
            self.bloomfilters.add( key=fp, set_value=1, transaction=True, timeout=None)
            return False



    def close(self, reason):
        """Delete data on close. Called by scrapy's scheduler"""
        self.clear()

    def clear(self):
        """Clears fingerprints data"""
        self.server.delete(self.key)
