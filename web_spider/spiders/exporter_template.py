import scrapy

class AmazonItem(scrapy.Item):
    rating = scrapy.Field()
    date = scrapy.Field()
    review = scrapy.Field()
    link = scrapy.Field()

class AmazonSpider(scrapy.Spider):

    name = "amazon"
    allowed_domains = ['amazon.co.uk']
    start_urls = ['http://www.amazon.co.uk/product-reviews/B0042EU3A2/' ]

    def parse(self, response):

        for sel in response.xpath('//table[@id="productReviews"]//tr/td/div'):

            item = AmazonItem()
            item['rating'] = sel.xpath('./div/span/span/span/text()').extract()
            item['date'] = sel.xpath('./div/span/nobr/text()').extract()
            item['review'] = sel.xpath('./div[@class="reviewText"]/text()').extract()
            item['link'] = sel.xpath('.//a[contains(.,"Permalink")]/@href').extract()
            yield item

        xpath_Next_Page = './/table[@id="productReviews"]/following::*//span[@class="paging"]/a[contains(.,"Next")]/@href'
        if response.xpath(xpath_Next_Page):
            url_Next_Page = response.xpath(xpath_Next_Page).extract()[0]
            request = scrapy.Request(url_Next_Page, callback=self.parse)
            yield request