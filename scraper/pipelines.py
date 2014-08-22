from psycopg2._psycopg import IntegrityError

__author__ = 'htm'


class SFGateTechBusiness(object):

	def process_item(self, item, spider):
		try:
			# source = ('Scrapy')
			item.save()
			return item
		except IntegrityError, e:
			spider.log(str(e))
			return None
