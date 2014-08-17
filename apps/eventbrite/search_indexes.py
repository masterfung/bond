from haystack.exceptions import SearchFieldError
from django.template import loader, Context
from haystack.indexes import SearchIndex

__author__ = '@masterfung'

from haystack import indexes
from apps.eventbrite.models import EventbriteOAuth

class EventbriteEventIndex(SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='search/indexes/eventbrite/eventbrite_text.txt')
    city = indexes.CharField(model_attr='city')
    event_url = indexes.CharField(model_attr='event_url')
    description = indexes.CharField(model_attr='event_description', null=True)

    content_auto = indexes.EdgeNgramField(model_attr='event_name')  # search population with some intelligence

    def get_model(self):
        return EventbriteOAuth

    def index_queryset(self, using=None):
        ''' Used when the entire index for model is updated. '''
        return self.get_model().objects.all()

    def prepare_template(self, obj):
        """
        Flattens an object for indexing.

        This loads2 a template
        (``search/indexes/{app_label}/{model_name}_{field_name}.txt``) and
        returns the result of rendering that template. ``object`` will be in
        its context.
        """
        if self.instance_name is None and self.template_name is None:
            raise SearchFieldError("This field requires either its instance_name variable to be populated or an explicit template_name in order to load the correct template.")

        if self.template_name is not None:
            template_names = self.template_name

            if not isinstance(template_names, (list, tuple)):
                template_names = [template_names]
        else:
            template_names = ['search/indexes/%s/%s_%s.txt' % (obj._meta.app_label, obj._meta.module_name, self.instance_name)]

        t = loader.select_template(template_names)
        return t.render(Context({'object': obj}))