import scrapy


class ParsblogSpider(scrapy.Spider):
    name = 'parsBlog'
    allowed_domains = ['habr.com']

    def __init__(self,nblogs:int):
        base = ['https://habr.com/ru/users/sobolevn/posts/page']
        urls = []


        nblogs = (int) (nblogs/20+ (nblogs%20 if 1 else 0))
        for i in range(nblogs):
            urls.append(base+str(i)+'/')
        self.start_urls = urls

    def parse(self, response):
        print("procesing:" + response.url)

        index = 0;
        length = 0;
        orders = []
        while True:
            response.url = self.start_urls[0] + str(index)
            orders += response.xpath("//article/@id").extract()
            if len(orders)<= length: break

            length = len(orders)

        orders = {'page': response.url,'idblogs' : orders }





        yield orders

    #def parseblogs(self,):



