from haystack.forms import ModelSearchForm
from time import timezone


class FutureModelSearchForm(ModelSearchForm):
    def search(self):
        sqs = super(FutureModelSearchForm, self).search()
        return sqs.filter(start_date__gte=timezone.now())

