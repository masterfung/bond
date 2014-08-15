__author__ = 'htm'

BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.spiders']

ITEM_PIPELINES = {'scraper.pipelines.SFGateTechBusiness': 1000,
                  }


