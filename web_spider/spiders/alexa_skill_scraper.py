import scrapy
from threading import Lock
import time
import io

lock = Lock()

class SpiderItem(scrapy.Item):
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
		yield scrapy.Request(url=self.cat_url, callback=self.parse_start)


	# deal with page turning
	# assuming there are > 3 pages in each category
	def parse_start(self, response):
		#yield scrapy.Request(url=response.url, callback=self.parse_category_page)

		# next page
		url_template = response.xpath('//span[@class=$val]//a/@href', val="pagnLink").extract_first()
		if url_template == None:
			return

		url_template = "https://www.amazon.com" + url_template.encode("utf-8")
		
		last_index = response.xpath('//span[@class=$val]/text()', val="pagnDisabled").extract_first()

		if last_index == None:
			return

		#print("last page: " + last_index + "  " + self.cat_name)
		if int(last_index) < 1:
			print("ERROR: too few pages")

		with io.open('output/urlfile.txt','a+', encoding='utf-8') as file:

			for i in range(1, int(last_index)+1):
				url = url_template.replace("&page=2", "&page="+str(i))
				file.write(u'%s' % url)
				file.write(u'\n')
				#yield scrapy.Request(url=url, callback=self.parse_category_page)

		file.close()

	# spawn threads to parse skill page
	def parse_category_page(self, response):
		print(response.status)
		urls = response.xpath('//a[contains(@class, $val)]/@href', val="s-access-detail-page").extract()
		print(response.url + "  " + str(len(urls)))

		with io.open('output/urlfile.txt','a+', encoding='utf-8') as file:
			for url in urls:
			#yield scrapy.Request(url=url, callback=self.parse_skill_page)
				file.write(u'%s' % url)
				file.write(u'\n')

		file.close() 


	# this function outputs data
	def parse_skill_page(self, response):
		category = self.cat_name
		categoryURL = self.cat_url
		
		skillName = response.xpath('//h1[@class=$val]/text()', val='a2s-title-content').extract_first()

		skillAuthor = response.xpath("//div[@id='a2s-product-info']//div[contains(@class, 'a2s-title')]//span/text()").extract_first()

		reviews = response.xpath('//span[contains(@class, $val)]/text()', val='totalReviewCount').extract_first()

		rating = response.xpath('//span[contains(@class, $val)]/text()', val='arp-rating-out-of-text').extract_first()
		
		quotes = response.xpath("//div[@class='a2s-utterance-box-inner']//span[@class='a2s-utterance-text']//em/text()").extract()

		quote1 = None
		quote2 = None
		if len(quotes) >= 1:
			quote1 = quotes[0]
		if len(quotes) >= 2:
			quote2 = quotes[1]

		skillURL = response.url

		description = response.xpath('//div[@id=$val]//span/text()', val='a2s-description').extract_first()

		item = SpiderItem()
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







