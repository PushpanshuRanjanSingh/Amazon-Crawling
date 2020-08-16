# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AzcrawlingItem(scrapy.Item):
    Title = scrapy.Field()
    Image = scrapy.Field()
    Stars = scrapy.Field()
    Price = scrapy.Field()