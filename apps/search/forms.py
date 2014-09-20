from haystack.forms import SearchForm
from django.utils import timezone


class FutureSearchForm(SearchForm):
    def search(self):
        sqs = super(FutureSearchForm, self).search()
        return sqs.filter(start_date__gte=timezone.now())

