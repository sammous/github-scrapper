# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from github_scrapper.items import GithubScrapperItem
from scrapy.http import *

class GithubSpider(scrapy.Spider):
	name = "github"
	allowed_domains = ["github.com"]
	language = ""

	def start_requests(self):

		def format_location(l):
			reformated_list = []
			for i in l:
				s = "location%3A%22" + i + "%22"
				reformated_list.append(s)
			return reformated_list

		#LIST OF LOCATIONS
		search_term_list_to_format = ["united+kingdom",
		"uk", "ireland",
		"scotland", "wales",
		"london", "manchester",
		"birmingham%22", "cambridge",
		"oxford","leeds",
		"scotland","southampton", "liverpool",
		"cardiff", "edinburgh",
		"dublin", "belfast",
		"germany", "france",
		"italy", "spain",
		"romania", "greece",
		"hungary", "czech+republic",
		"slovakia", "poland",
		"bulgaria", "slovenia",
		"croatia", "austria",
		"lithuania", "latvia",
		"estonia"]

		search_term_list = format_location(search_term_list_to_format)

		skills = ["Javascript", "Python","C%23","C","CSS","HTML","Ruby","PHP","Java","Shell","C%2B%2B"]

		#Sort filter, order : best matches, followers, repos
		search_filter = ["","followers","joined","repositories"]

		for skill in skills:
			if skill == "C%23":
				self.language = "csharp"
			elif skill == "C%2B%2B":
				self.language = "C++"
			else:
				self.language = skill
			for place in search_term_list:
				for i in range(1,100):
					for j in range(8):
						if j < 4 :
							#order asc
							url = "https://github.com/search?l="+skill+"&o=asc"+"&p="+str(i)+"&q="+place+"&ref=searchresults&s="+search_filter[j]+"&type=Users&utf8=✓"
							yield Request(url, self.parse)
						else:
							j = j%4
							#order desc
							url = "https://github.com/search?l="+skill+"&o=desc"+"&p="+str(i)+"&q="+place+"&ref=searchresults&s="+search_filter[j]+"&type=Users&utf8=✓"
							yield Request(url, self.parse)


	def parse(self, response):

		items = []

		for users in response.xpath('//div[@class="user-list-item"]'):
			email = users.xpath('.//div[@class="user-list-info"]/ul/li[2]/span/a/text()').extract()
			username = users.xpath('.//div[@class="user-list-info"]/a/text()').extract()
			location = users.xpath('.//div[@class="user-list-info"]/ul/li[1]/text()').extract()
			name = users.xpath('.//*/text()').extract()
			image = users.xpath('.//a/img/@src').extract()
			joined = users.xpath('//div[@class="user-list-info"]/ul/li[3]/span/local-time/text()').extract()

			item = GithubScrapperItem()

			if len(email)==0:
				item['email'] = u"null"
			else:
				item['email'] = email[0]

			if len(location)>1:
				location[0] = location[0].strip().strip('\n')
				location[1] = location[1].strip().strip('\n')
				
			item['location'] = ','.join(location)[1:]
 			item['language'] = self.language
 			item['name'] = name[0].strip("\n ")
 			item['joined'] = joined[0]
 			item['username'] = username[0]
 			item['image'] = image[0]

			self.logger.info(item)

		return item
