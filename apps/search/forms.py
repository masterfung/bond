from haystack.forms import SearchForm
from django.utils import timezone
from apps.profiles.models import UserCity


class FutureSearchForm(SearchForm):
    """Override the FutureSearchForm to show the dates that are greater than or equal to today.
    This insures events are most recent."""
    def search(self):
        sqs = super(FutureSearchForm, self).search()
        return sqs.filter(start_dateTime__gte=timezone.now())

