from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scraper.items import SFGateTechBusiness

__author__ = 'htm'


class SFGate(BaseSpider):
	name = 'sf_gate_tech_business'
	allowed_domains = ['events.sfgate.com/']
	start_urls = [
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&ssi=50&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&ssi=100&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&ssi=150&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&ssi=200&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&ssi=250&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&ssi=300&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&ssi=350&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&ssi=400&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&ssi=450&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&ssi=500&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&ssi=550&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&ssi=600&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&ssi=650&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&ssi=700&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
		'http://events.sfgate.com/search?cat=3&new=n&sort=0&srad=85.0&srss=50&ssi=750&st=event&svt=text&swhat=&swhen=&swhere=San+Francisco%2C+CA',
	]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.xpath(".//table[@class='search_result_table']")
		items = []
		for title in titles:
			event = SFGateTechBusiness()
			event['url'] = title.xpath(".//td[@class='title_content']/a/@href").extract()[0].strip().replace('"', '')
			event['title_content'] = title.xpath(".//td[@class='title_content']/a/text()").extract()[0].strip().replace(
				'"', '')
			event['description_content'] = title.xpath(".//td[@class='description_content']/div/text()").extract()[
				0].strip().replace('"', '')
			event['meta_date_content'] = title.xpath(".//td[@class='meta_content']/div[1]/text()").extract()[
				0].strip().replace('"', '')
			event['meta_event_link'] = title.xpath(".//td[@class='meta_content']/div[2]/a/@href").extract()[
				0].strip().replace('"', '')
			event['meta_event_location'] = title.xpath(".//td[@class='meta_content']/div[2]/a/text()").extract()[
				0].strip().replace('"', '')
			# event['buy_link'] = title.xpath("//td[@class='meta_content']/div[2]/a/@href").extract()
			items.append(event)
		return items