from haystack.indexes import SearchIndex
from scraper.models import Scraper

__author__ = 'htm'

# from haystack import Indexes
#
#
# class SFGateScraperIndex(SearchIndex, Indexes.Indexable):
#     text = Indexes.CharField(document=True, use_template=True)
#     name = Indexes.CharField(model_attr='name')
#     url = Indexes.CharField(model_attr='url')
#     description = Indexes.CharField(model_attr='description_content', null=True)
#
#     content_auto = Indexes.EdgeNgramField(model_attr='event_name')  # search population with some intelligence
#
#     def get_model(self):
#         return Scraper
#
#     def index_queryset(self, using=None):
#         ''' Used when the entire index for model is updated. '''
#         return self.get_model().objects.all()