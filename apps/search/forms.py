from haystack.forms import SearchForm
from django.utils import timezone
from apps.profiles.models import UserCity


class FutureModelSearchForm(SearchForm):

    def search(self):
        sqs = super(FutureModelSearchForm, self).search()
        return sqs.filter(start_date__gte=timezone.now())

