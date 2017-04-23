import scrapy


class QuotesSpider(scrapy.Spider):
    name = "jdtest"
    start_urls = [
        'https://item.jd.com/3995645.html',
    ]

    def parse(self, response):
        yield {
            'name':response.css('.parameter2 li:nth-child(1)::text').extract(),
            'id':response.css('.parameter2 li:nth-child(2)::text').extract(),
        }