# - * - coding: utf-8 - * -

from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from BookSpider.items import BookspiderItem
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class BookContentSpider(RedisSpider):
    name = 'BookContentSpider'
    redis_key = "BookContentSpider:start_urls"

    def parse(self, response):
        item = BookspiderItem()
        selector = Selector(response)
        book_id = str(re.search('subject/(.*?)/',response.url).group(1))
        title = selector.xpath('//h1/span/text()').extract()
        author = selector.xpath("//div[@id='info']/a[1]/text()").extract()
        if author:
            author = author[0].replace(' ','').replace('\n','')
        else:
            author = selector.xpath("//div[@id='info']/span[1]/a/text()").extract()
            author = author[0].replace(' ','').replace('\n','')
        info = selector.xpath("//div[@id='info']").extract()
        info = ''.join(info).replace(' ','').replace('\n','')
        info = info.decode('utf-8')
        isbn13 = re.search('ISBN:</span>(.*?)<br>',info)
        if isbn13:
            isbn13 = str(isbn13.group(1))
        else:
            isbn13 = ''
        publisher =str(re.search(u'\u51fa\u7248\u793e:</span>(.*?)<br>',info).group(1))
        pubdate = str(re.search(u'\u51fa\u7248\u5e74:</span>(.*?)<br>',info).group(1))
        price = re.search(u'\u5b9a\u4ef7:</span>(.*?)<br>',info)
        if price:
            price = str(price.group(1))
        else:
            price = ''
        pages = re.search(u'\u9875\u6570:</span>(.*?)<br>',info)
        if pages:
            pages = str(pages.group(1))
        else:
            pages = ''
        translator = re.search(u'\u8bd1\u8005:</span>(.*?)<br>', info)
        if translator:
            translator = str(re.search(u'>(.*?)</a>', translator.group(1)).group(1))
        else:
            translator = ''
        summary = selector.xpath("//div[@class='indent']/span[@class='all hidden']").extract()
        if summary:
            summary = re.findall(u'<p>(.*?)</p>', summary[0])
        else:
            summary = selector.xpath("//div[@class='intro']/p/text()").extract()

        catalog = selector.xpath("//div[@id='dir_"+book_id+"_full']/text()").extract()
        if catalog:
            # delete useless dot
            catalog.pop()
            catalog.pop()
        else:
            catalog=''

        lookcount = selector.xpath("//div[@id='collector']/p[contains(@class, 'pl')][2]/a/text()").extract()
        lookcount = ''.join(lookcount)
        lookcount = str(re.search(u'(\d+)',lookcount).group(1))
        image = selector.xpath("//a[@class = 'nbg']/img/@src").extract()
        tryread = selector.xpath("//div[@class='indent']/div/a/@href").extract()

        short_review_content = selector.xpath("//p[@class='comment-content']/text()").extract()
        short_review_name = selector.xpath("//span[@class='comment-info']/a/text()").extract()
        short_review_id = selector.xpath("//span[@class='comment-info']/a/@href").extract()
        if short_review_id:
            for index,id in enumerate(short_review_id):
                short_review_id[index] = str(re.search('https://www.douban.com/people/(.*?)/',id).group(1))
        else:
            short_review_id = ''

        review_title = selector.xpath("//a[@class='title-link']/text()").extract()
        review_link = selector.xpath("//a[@class='title-link']/@href").extract()
        review_name = selector.xpath("//a[@class='author']/span/text()").extract()
        review_id = selector.xpath("//a[@class='author']/@href").extract()
        if review_id:
            for index,id in enumerate(review_id):
                review_id[index] = str(re.search('https://www.douban.com/people/(.*?)/',id).group(1))
        else:
            review_id = ''

        if len(tryread) >= 4:
            tryread = tryread[3]
        else:
            tryread = ''

        item['book_id'] = book_id
        item['title'] = title
        item['author'] = author
        item['image'] = image

        item['isbn13'] = isbn13
        item['publisher'] = publisher
        item['pubdate'] = pubdate
        item['price'] = price
        item['pages'] = pages
        if translator:
            item['translator'] = translator
        else:
            item['translator'] = ''
        item['summary'] = summary
        item['catalog'] = catalog
        item['lookcount'] = lookcount
        if len(tryread) >= 4:
            item['tryread'] = tryread
        else:
            item['tryread'] = tryread

        item['short_review_content'] = short_review_content
        item['short_review_name'] = short_review_name
        item['short_review_id'] = short_review_id

        item['review_title'] = review_title
        item['review_link'] = review_link
        item['review_name'] = review_name
        item['review_id'] = review_id
        yield item
