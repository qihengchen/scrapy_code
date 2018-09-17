import scrapy
from threading import Lock
import time

lock = Lock()

class SpiderItem(scrapy.Item):
	ItemID = scrapy.Field()
	Category = scrapy.Field()
	CategoryURL = scrapy.Field()
	SkillName = scrapy.Field()
	SkillAuthor = scrapy.Field()
	Reviews = scrapy.Field()
	Rating = scrapy.Field()
	Quote1 = scrapy.Field()
	Quote2 = scrapy.Field()
	SkillURL = scrapy.Field()
	Description = scrapy.Field()

class AlexaSkillsSpider(scrapy.Spider):
	name = "amazon_spider"

	# grab detail pages
	def start_requests(self):
		yield scrapy.Request(url=self.cat_url, callback=self.parse_category_page)

		#time.sleep(30)
		#print(self.count)

	def parse_startup(self, response):
		print(response.url)
		# next page
		next_url = response.xpath('//span[@class=$val]//a/@href', val="pagnLink").extract_first()
		next_url = "https://www.amazon.com" + next_url.encode("utf-8")
		print(next_url)
		last_index = response.xpath('//span[@class=$val]/text()', val="pagnDisabled").extract_first()
		print("last page " + last_index)
		# &page=n


	def parse_category_page(self, response):
		# <a class contains s-access-detail-page. parse href
		# extract skill page urls from category page
		
		urls = response.xpath('//a[contains(@class, $val)]/@href', val="s-access-detail-page").extract()
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse_detail_page)

	# this function outputs data
	def parse_detail_page(self, response):
		itemID = response.xpath('//h1[@class='a2s-title-content']/text()').extract_first()
		if itemID: itemID = itemID.encode("utf-8")

		category = self.cat_name
		categoryURL = self.cat_url
		
		skillName = response.xpath('//div[@class='a2s-title']//h1/text()').extract_first()

		skillAuthor = response.xpath('//div[@class='a2s-title']//span/text()').extract_first()

		reviews = response.xpath('//span[contains(@class, 'totalReviewCount')]/text()').extract_first()

		rating = response.xpath('//span[contains(@class, 'arp-rating-out-of-text')]/text()').extract_first()
		
		quotes = response.xpath('//div[@class='a2s-utterance-box-inner')]//span[@class='a2s-utterance-text']//em/text()').extract()
		quote1 = None
		quote2 = None
		if len(quotes) == 1:
			quote1 = quotes[0]
		elif len(quotes) == 2:
			quote1 = quotes[0]
			quote2 = quotes[1]

		skillURL = response.url

		description = xpath('//div[@id='a2s-description')]//span/text()').extract_first()

		item = SpiderItem()
		item['ItemID'] = itemID
		item['Category'] = category
		item['CategoryURL'] = categoryURL
		item['SkillName'] = skillName
		item['SkillAuthor'] = skillAuthor
		item['Reviews'] = reviews
		item['Rating'] = rating
		item['Quote1'] = quote1
		item['Quote2'] = quote2
		item['SkillURL'] = skillURL
		item['Description'] = description
		yield item







