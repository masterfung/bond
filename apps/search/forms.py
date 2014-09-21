from haystack.forms import SearchForm
from django.utils import timezone
from apps.profiles.models import UserCity


<<<<<<< HEAD
class FutureModelSearchForm(SearchForm):

=======
class FutureSearchForm(SearchForm):
>>>>>>> FETCH_HEAD
    def search(self):
        sqs = super(FutureSearchForm, self).search()
        return sqs.filter(start_date__gte=timezone.now())

