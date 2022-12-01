import scrapy

class NamesBlogSpider:


    def __init__(self,url = '@sobolevn'):
        self.url = 'https://habr.com/ru/users/'+url[1:]+'/posts/page1/'


    def parse(self, response):
        print("procesing:" + response.url)

        orders = response.xpath("//article/@id").extract()
        print(orders)


