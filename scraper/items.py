import scrapy
from scrapy.item import Item, Field


class SFGateTechBusiness(Item):
	url = scrapy.Field()
	title_content = scrapy.Field()
	description_content = scrapy.Field()
	meta_date_content = scrapy.Field()
	meta_event_link = scrapy.Field()
	meta_event_location = scrapy.Field()
