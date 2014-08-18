from json import dumps
import json
from django.views.decorators.csrf import csrf_exempt
from requests_oauthlib import OAuth2Session
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from requests import get
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from apps.meetup.forms import TopicEventIndexForm
from models import TopicEvent
from apps.meetup.serializer import TopicEventSerializer
# from .permissions import IsOwnerOrReadOnly
from haystack.query import SearchQuerySet
# from settings import local
from tasks import hello_world
from django.views.generic import TemplateView


# permission_classes = (IsOwnerOrReadOnly,)
#
# def get(self, request, *args, **kwargs):
# return self.list(request, *args, **kwargs)
#
# def post(self, request, *args, **kwargs):
# return self.create(request, *args, **kwargs)


# class EventList(EventMixin, ListCreateAPIView):
# pass
#
#
# class EventDetail(EventMixin, RetrieveUpdateDestroyAPIView):
# pass


# MEETUP_API_KEY = local.MEETUP_API_KEY

ACCESS_TOKEN_URL = 'https://secure.meetup.com/oauth2/access'
AUTHORIZATION_URL = 'https://secure.meetup.com/oauth2/authorize'
REDIRECT_URI = 'bondandme.com'


@csrf_exempt
def meetup_oauth_connect(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		print "{} is the token".format(data)

	client_id = 'vjrn056elr2s00femc9i9smmhf'
	client_secret = 'puv15odjlhhpcr4ja42j16e2vq'

	scope = ACCESS_TOKEN_URL
	oauth = OAuth2Session(client_id, redirect_uri=REDIRECT_URI)

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


# def notes(request):
# form = TopicEventIndexForm(request.GET)
# events = form.search()
# return render(request, 'events/events.html', {'events': events})


@login_required
def events(request):
	events = TopicEvent.objects.all()
	return render(request, 'events/events.html')


@login_required
def event(request, topicevent_id=1):
	return render(request, 'events/event.html', {'event': TopicEvent.objects.get(id=topicevent_id)})


@login_required
def search_titles(request):
	topic_event = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))

	return render(request, 'events/events.html', {'topic_event': topic_event})


class IndexView(TemplateView):
	template_name = 'events/events.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		hello_world()
		return context


class EventMixin(object):
	queryset = TopicEvent.objects.all()
	serializer_class = TopicEventSerializer(queryset)


# @api_view(['GET', 'POST'])
# def event_list(request):
# '''
# List all events, or create a new event.
# '''
#
# if request.method == 'GET':
# events = TopicEvent.objects.all()
# serializer = TopicEventSerializer(events)
# return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TopicEventSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 serializer._errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def event_detail(request, pk):
#     try:
#         event = TopicEvent.objects.get(pk=pk)
#     except TopicEvent.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = TopicEventSerializer(event)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = TopicEventSerializer(event, data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         event.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

