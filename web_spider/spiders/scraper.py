import scrapy

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

	metadata = {
		"Arts & lifestyle": (7, "OtherLifestyle"),
		"Business & finance": (2, "OtherBusinessAndFinance"),
		"Education & reference": (3, "OtherEducationAndReference"),
		"Food & drink": (4, "OtherFood"),
		"Games & fun": (5, "OtherGames"),
		"Health & fitness": (6, "OtherHealthAndFitness"),
		"Home control": (19, "OtherHomeControl"),
		"Kids & family": (20, "OtherKidsAndFamily"),
		"Local": (8, "OtherLocal"),
		"Movies, photos & TV": (9, "OtherMoviesAndTv"),
		"Music & audio": (10, "OtherMusicAndAudio"),
		"News & magazines": (1, "OtherNews"),
		"Productivity": (12, "OtherProductivity"),
		"Shopping": (13, "OtherShopping"),
		"Social & communication": (14, "OtherSocial"),
		"Sports": (15, "OtherSports"),
		"Travel & transportation": (16, "OtherTravelAndTransportation"),
		"Weather": (18, "OtherWeather")
	}

	# conventions
	# field: "Arts & lifestyle"
	# sub_field: "Get info about arts and culture"
	# action: "Book Author Facts"

	# urls - ["url1", "url2"...]
	def start_requests(self):
		#for i in range(20):
			#field_url = "https://assistant.google.com/explore/c/" + str(i) + "/?hl=en"
		#field_urls = ["https://assistant.google.com/explore/c/7/?hl=en"]
		
		for field, v in self.metadata.items():
			print(field)
			url = "https://assistant.google.com/explore/c/%d/?hl=en" % v[0]
			other_page_url = "https://assistant.google.com/explore/i?intent=%s&hl=en-US" % v[1]
			#req = scrapy.Request(url=url, callback=lambda r: self.parse_field_page(r, field))
			req1 = scrapy.Request(url=url, callback=self.parse_field_page)
			req1.meta['field'] = field
			yield req1
			req2 = scrapy.Request(url=other_page_url, callback=self.parse_sub_field_page)
			req2.meta['field'] = field
			yield req2


	def parse_field_page(self, response):
		field = response.request.meta['field']
		#print(field)
		# extract "View More" urls
		headers = response.xpath('//span[contains(@role, "heading")]/text()').extract()
		#print("--- Headers --- ", type(headers))
		#print(headers)
		sub_field_urls = {}
		for header in headers:
			sub_field = header.encode("ascii")
			sub_field_urls[sub_field] = self.prep_sub_field_url(sub_field)

		# [example] https://assistant.google.com/explore/i?intent=CheckHoroscopes&hl=en-US
		for k, url in sub_field_urls.items():
			req = scrapy.Request(url=url, callback=self.parse_sub_field_page)
			req.meta['field'] = field
			yield req


	def parse_sub_field_page(self, response):
		field = response.request.meta['field']
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

			req = scrapy.Request(url=url, callback=self.parse_action_page)
			req.meta['field'] = field
			yield req

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
		field = response.request.meta['field']
		action = response.xpath('//div[@class=$val]/text()', val="YtWsM RfR9R").extract_first()
		if action: action = action.encode("utf-8") 
		description = response.xpath('//div[@class=$val]/text()', val="IB9ccf").extract_first()
		if description: description = description.encode("utf-8")
		rating = response.xpath('//div[@class=$val]/text()', val="NRNQAb FTlnHb").extract_first()
		if rating: rating = rating.encode("utf-8")
		users = response.xpath('//div[@class=$val]/text()', val="rriIab CdFZQ").extract_first()
		if users: users = users.encode("utf-8")
		developer = response.xpath('//div[@class=$val]/text()', val="lUcxUb CbqDob").extract_first()
		if developer: developer = developer.encode("utf-8")

		item = SpiderItem()
		item['Field'] = field
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



