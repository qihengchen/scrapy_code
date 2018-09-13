import scrapy

#TODO: fetch "Other" subfields, output 'Field' column

class SpiderItem(scrapy.Item):
	Field = scrapy.Field()
	Action = scrapy.Field()
	Description = scrapy.Field()
	Rating = scrapy.Field()
	Users = scrapy.Field()
	Developer = scrapy.Field()


class GoogleAssistantSpider(scrapy.Spider):
	name = "web_spider"

	field_class_id = "tqwMZ VoIGZc"
	action_class_id = "YtWsM RfR9R"
	description_class_id = "IB9ccf"
	rating_class_id = "NRNQAb FTlnHb"
	users_class_id = "rriIab CdFZQ"
	developer_class_id = "lUcxUb CbqDob"
	data_link_class_id = "vsao6c"

	field = "Arts & lifestyle"

	# conventions
	# field: "Arts & lifestyle"
	# sub_field: "Get info about arts and culture"
	# action: "Book Author Facts"

	# urls - ["url1", "url2"...]
	def start_requests(self):
		
		field_urls = ["https://assistant.google.com/explore/c/7/?hl=en"]

		for url in field_urls:
			yield scrapy.Request(url=url, callback=self.parse_field_page)


	def parse_field_page(self, response):
		# extract "View More" urls
		headers = response.xpath('//span[contains(@role, "heading")]/text()').extract()
		print("--- Headers --- ", type(headers))
		print(headers)
		sub_field_urls = {}
		for header in headers:
			sub_field = header.encode("ascii")
			sub_field_urls[sub_field] = self.prep_sub_field_url(sub_field)

		# [example] https://assistant.google.com/explore/i?intent=CheckHoroscopes&hl=en-US
		for k, url in sub_field_urls.items():
			yield scrapy.Request(url=url, callback=self.parse_sub_field_page)
		

	def parse_sub_field_page(self, response):
		# data-link="services/a/uid/000000207e4476cb?hl=en"
		# [example] https://assistant.google.com/services/a/uid/000000207e4476cb?hl=en
		data_links = response.xpath('//div[@class=$val]/@data-link', val="vsao6c").extract()
		#data_links = [data_links]
		#print("--- Data Link ---")
		#print(data_links, "size: ", len(data_links))

		for data_link in data_links:
			if data_link == None:
				continue

			data_link = data_link.encode("ascii")
			url = self.prep_action_url(data_link)

			yield scrapy.Request(url=url, callback=self.parse_action_page)

	# this function outputs data
	def parse_action_page(self, response):
		"""
		field_class_id = "tqwMZ VoIGZc"
		action_class_id = "YtWsM RfR9R"
		description_class_id = "IB9ccf"
		rating_class_id = "NRNQAb FTlnHb"
		users_class_id = "rriIab CdFZQ"
		developer_class_id = "lUcxUb CbqDob"
		"""
		#field = response.xpath('//div[@class=$val]/text()', val="tqwMZ VoIGZc").extract()
		action = response.xpath('//div[@class=$val]/text()', val="YtWsM RfR9R").extract_first().encode("utf-8")
		description = response.xpath('//div[@class=$val]/text()', val="IB9ccf").extract_first().encode("utf-8")
		rating = response.xpath('//div[@class=$val]/text()', val="NRNQAb FTlnHb").extract_first().encode("utf-8")
		users = response.xpath('//div[@class=$val]/text()', val="rriIab CdFZQ").extract_first().encode("utf-8")
		developer = response.xpath('//div[@class=$val]/text()', val="lUcxUb CbqDob").extract_first()
		if developer != None:
			developer = developer.encode("utf-8")

		item = SpiderItem()
		item['Field'] = self.field
		item['Action'] = action
		item['Description'] = description
		item['Rating'] = rating
		item['Users'] = users
		item['Developer'] = developer
		yield item


	# u'Check horoscopes' -> "CheckHoroscopes"
	def prep_sub_field_url(self, sub_field):
		# capitalize first char and rip off spaces
		sub_field = sub_field.title().replace(" ", "")
		# Warning: prepared printf might run faster than sting concatenation
		url = "https://assistant.google.com/explore/i?intent=" + sub_field + "&hl=en-US"
		return url


	def prep_action_url(self, data_link):
		return "https://assistant.google.com/" + data_link



