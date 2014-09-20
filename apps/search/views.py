from haystack.views import SearchView as HaystackSearchView

from apps.search.forms import FutureModelSearchForm


class SearchView(HaystackSearchView):
    form = FutureModelSearchForm

