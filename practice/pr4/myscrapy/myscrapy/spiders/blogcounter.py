import scrapy


class BlogcounterSpider(scrapy.Spider):
    name = 'blogcounter'
    allowed_domains = ['habr.com']

    def __init__(self,sturl):
        self.start_urls = 'https://habr.com/ru/users/{0}/posts/'.format(sturl[1:])


    def parse(self, response):
        print("procesing:" + response.url)

        count = response.xpath('//img[starts-with(@class, "tm-tabs__tab-counter")]')


