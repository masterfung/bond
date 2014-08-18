from haystack.indexes import SearchIndex
from scraper.models import Scraper

__author__ = 'htm'

# from haystack import indexes
#
#
# class SFGateScraperIndex(SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     name = indexes.CharField(model_attr='name')
#     url = indexes.CharField(model_attr='url')
#     description = indexes.CharField(model_attr='description_content', null=True)
#
#     content_auto = indexes.EdgeNgramField(model_attr='event_name')  # search population with some intelligence
#
#     def get_model(self):
#         return Scraper
#
#     def index_queryset(self, using=None):
#         ''' Used when the entire index for model is updated. '''
#         return self.get_model().objects.all()