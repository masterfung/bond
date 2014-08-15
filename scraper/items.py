import scrapy
from scrapy.contrib.djangoitem import DjangoItem
from scrapy.item import Item, Field
from models import Scraper


# class SFGateTechBusiness(Item):
# 	url = Field()
# 	title_content = Field()
# 	description_content = Field()
# 	meta_date_content = Field()
# 	meta_event_link = Field()
# 	meta_event_location = Field()


class SFGateTechBusiness(DjangoItem):
	django_model = Scraper