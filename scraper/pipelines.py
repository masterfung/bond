from psycopg2._psycopg import IntegrityError

__author__ = 'htm'


class SFGatePipeline(object):

	def process_item(self, item, spider):
		try:
			item.save()
			return item
		except IntegrityError, e:
			spider.log(str(e))
			return None
