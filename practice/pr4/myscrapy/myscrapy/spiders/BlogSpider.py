import scrapy


class BlogSpiderSpider(scrapy.Spider):
    name = 'blogcounter'
    allowed_domains = ['habr.com']

    def __init__(self,sturl):
        start_urls = sturl

    def parse(self, response):
        pass
