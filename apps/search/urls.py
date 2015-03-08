from __future__ import unicode_literals
from apps.search.forms import FutureSearchForm

try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url

from haystack.views import SearchView


urlpatterns = patterns('haystack.views',
                       url(r'^$', SearchView(form_class=FutureSearchForm), name='haystack_search'),
)