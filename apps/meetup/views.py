import json
import logging
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
# from apps.meetup.forms import EventIndexForm
from rest_framework.permissions import IsAuthenticated
from models import Event
from oauth2_provider.views.generic import ProtectedResourceView
from apps.meetup.serializer import EventSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from haystack.query import SearchQuerySet
from tasks import hello_world
from django.views.generic import TemplateView


logger = logging.getLogger(__name__)


@csrf_exempt
def meetup_oauth_connect(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print "{} is the token".format(data)

    # client_id = 'vjrn056elr2s00femc9i9smmhf'
    # client_secret = 'puv15odjlhhpcr4ja42j16e2vq'

    # scope = ACCESS_TOKEN_URL
    # oauth = OAuth2Session(client_id, redirect_uri=REDIRECT_URI)

    # r = oauth.get(AUTHORIZATION_URL)
    # print r
    # token = oauth.fetch_token(ACCESS_TOKEN_URL, client_secret)
    # print token

    # meetup = OAuth2Session(client_id)
    # authorization_url, state = meetup.authorization_url(AUTHORIZATION_URL)
    # print state
    #
    # callback = OAuth2Session(client_id, state=state)
    # token = callback.fetch_token(ACCESS_TOKEN_URL, client_secret=client_secret, authorization_response="/")
    # print "{} is the token".format(token)


    return render(request, 'meetup/meetup_oauth.html')

@csrf_exempt
def autocomplete(request):
    """

    """
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:5]
    suggestions = [result.event_name for result in sqs]
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')


@login_required
def events(request):
    """

    """
    events = Event.objects.all()
    return render(request, 'events/events.html')


@login_required
def event(request, event_id=1):
    """

    """
    return render(request, 'events/event.html', {'event': Event.objects.get(id=event_id)})


@login_required
def search_titles(request):
    """

    """
    event = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))

    return render(request, 'events/events.html', {'event': event})


class IndexView(TemplateView):
    """

    """
    template_name = 'events/events.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        hello_world()
        return context


class EventMixin(object):
    """
    This EventMixin is used for Bond's events.
    This code is recycled across different classes. It makes
    the most sense to abstract this out and use a mixin, as
    shown here.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventList(EventMixin, generics.ListCreateAPIView):
    """
    List all events in the DB, or allows the
    users to create new events.
    """
    permission_classes = (IsAuthenticated,)


class EventDetail(EventMixin, generics.RetrieveUpdateDestroyAPIView):
    """

    """
    permission_classes = (IsAdminUser,)


class ApiEndpoint(ProtectedResourceView):
    """

    """
    def get(self, request, *args, **kwargs):
        return HttpResponse('Protected with Oauth2!')
