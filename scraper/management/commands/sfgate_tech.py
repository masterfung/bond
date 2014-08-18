from __future__ import absolute_import
import os
from django.core.management.base import BaseCommand
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scraper.items import SFGateTechBusiness

__author__ = 'htm'


class Command(BaseCommand):

	def run_from_argv(self, argv):
		self._argv = argv
		return super(Command, self).run_from_argv(argv)

	def handle(self, *args, **options):
		os.environ['SCRAPY_SETTINGS_MODULE'] = args[0]
		from scrapy.cmdline import execute
		execute(self._argv[1:])