# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogItem(scrapy.Item):
    url = scrapy.Item()
    title = scrapy.Field()
    subtitle = scrapy.Field();
    description = scrapy.Field();
