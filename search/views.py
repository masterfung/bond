from haystack.views import SearchView as HaystackSearchView
from search.forms import FutureModelSearchForm


class SearchView(HaystackSearchView):
    form = FutureModelSearchForm

