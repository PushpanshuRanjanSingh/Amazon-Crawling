import scrapy
from ..items import AzcrawlingItem
import os,json

class maxPagination(Exception):
    pass

class AZCrawling(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    flag = 0
    # start_urls = ['https://www.amazon.com/s?k=shirts+for+men&page=1']
    url = input("What you Want to search : ")
    url = url.replace(' ','+')
    start_urls = ['https://www.amazon.com/s?k='+url+'&s=relevanceblende'+'&page=1']
    print(start_urls)
    if os.path.exists("AmazonCrawlData.json"):
        os.remove('AmazonCrawlData.json')
    if os.path.exists("RefineJSON.json"):
        os.remove('RefineJSON.json')

    custom_settings ={
        'FEED_FORMAT' : 'json',
        'FEED_URI' : 'AmazonCrawlData.json'
    }

    def parse(self, response):
        items = AzcrawlingItem()

        Title = response.css('.a-color-base.a-text-normal::text').extract()
        Image = response.css('.s-image::attr(src)').extract()
        Stars = response.css('span.a-icon-alt::text').extract()
        Price = response.css('span.a-price').css('span.a-offscreen::text').extract()

        items['Title'] = Title
        items['Image'] = Image
        items['Stars'] = Stars
        items['Price'] = Price
        yield items
        
        next_page = 'https://www.amazon.com/s?k='+AZCrawling.url+'&s=relevanceblende'+'&page='+str(AZCrawling.page_number)+"'"
        if AZCrawling.page_number<30:
            try:
                if response.css('.a-color-base.a-text-normal').css('::text').extract() == []:
                    raise maxPagination
                AZCrawling.page_number+=1
                yield response.follow(next_page, callback=self.parse)
            except maxPagination:
                print('Items are no more available')

