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
from settings import local
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


MEETUP_API_KEY = local.MEETUP_API_KEY

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


@login_required
@csrf_exempt
# @user_passes_test(lambda u: u.is_superuser)
def meetup_open_events(request):
	offset = 1
	data_to_return = []
	datacode = []
	if request.method == 'POST':
		data = json.loads(request.body)
		print data
		datacode.append(data)

	while offset < 20:
		offset += 1

		locations = [
			{'city': "los angeles", 'state': "ca", 'country': "us"},
			# {'city': "boston", 'state': "ma", 'country': "us"},
			{'city': "san francisco", 'state': "ca", 'country': "us"},
			{'city': "chicago", 'state': "il", 'country': "us"},
			{'city': "houston", 'state': "tx", 'country': "us"},
			{'city': "atlanta", 'state': "ga", 'country': "us"},
			{'city': "dallas", 'state': "tx", 'country': "us"},
			{'city': "seattle", 'state': "wa", 'country': "us"},
			{'city': "miami", 'state': "fl", 'country': "us"},
			{'city': "new york", 'state': "ny", 'country': "us"},
			{'city': "washington", 'state': "dc", 'country': "us"},
			{'city': "philadelphia", 'state': "pa", 'country': "us"},
			{'city': "phoenix", 'state': "az", 'country': "us"},
			{'city': "san antonio", 'state': "tx", 'country': "us"},
			{'city': "dallas", 'state': "tx", 'country': "us"},
			{'city': "san diego", 'state': "ca", 'country': "us"},
			{'city': "columbus", 'state': "oh", 'country': "us"},
			{'city': "charlotte", 'state': "nc", 'country': "us"},
			{'city': "indianapolis", 'state': "in", 'country': "us"},
			{'city': "memphis", 'state': "tn", 'country': "us"},
			{'city': "denver", 'state': "co", 'country': "us"},
			{'city': "portland", 'state': "or", 'country': "us"},
			{'city': "baltimore", 'state': "md", 'country': "us"},
			{'city': "las vegas", 'state': "nv", 'country': "us"},
			# {'city': "tuscan", 'state': "az", 'country': "us"},
			{'city': "jacksonville", 'state': "fl", 'country': "us"},
			{'city': "austin", 'state': "tx", 'country': "us"},
			{'city': "nashville", 'state': "tn", 'country': "us"},
			{'city': "cleveland", 'state': "oh", 'country': "us"},
			{'city': "new orleans", 'state': "la", 'country': "us"},
			{'city': "milwaukee", 'state': "wi", 'country': "us"},
		]

		for place in locations:
			resp = get("https://api.meetup.com/2/open_events.json",
			           params={
				           "key": MEETUP_API_KEY,
				           "city": place['city'],
				           "state": place['state'],
				           "country": "us",
				           "page": 200,
			               "radius": 50.0,
				           "offset": offset,
			           }, headers={
					# "Authorization": "Bearer {}".format(datacode[0])
				})

			if resp.status_code != 200:
				print "error"
				return

			data = dumps(resp.json(), indent=2, sort_keys=True)
			data_to_return.append(data)
			print data

			events = json.loads(data)
			print events

			events = events['results']

			x = 0
			while x <= 200:
				x += 1
				print x
				if not (len(events) > x):
					break

				event = events[x]

				if event.get('name'):
					meetup = TopicEvent.objects.get_or_create(
						group_id=event.get('group', {}).get('id', 'Not Available'),
						join_mode=event.get('group', {}).get('join_mode', 'Not Available'),
						group_name=event.get('group', {}).get('name', 'Not Available'),
						event_name=event.get('name', 'Not Available'),
						description=event.get('description', 'Not Available').strip(),
						group=event.get('group', 'Not Available'),
						venue=event.get('venue', 'Not Available'),
						event_id=event.get('id', 'Not Available'),
						updated=event.get('updated', None),
						visibility=event.get('visibility', 'Not Available'),
						status=event.get('status', 'Not Available'),
						utc_offset=event.get('utc_offset', None),
						rsvp_limit=event.get("rsvp_limit", 0),
						event_url=event.get('event_url', 'Not Available'),
						how_to_find_us=event.get('how_to_find_us', 'Not Available'),
						duration=event.get('duration', None),
						lat=event.get('venue', {}).get('lat', 0),
						lon=event.get('venue', {}).get('lon', 0),
						event_address=event.get('venue', {}).get('address_1', 'Not Available'),
						city=event.get('venue', {}).get('city', 'Not Available'),
						state=event.get('venue', {}).get('state', 'Not Available'),
						zip=event.get('venue', {}).get('zip', 0),
						country=event.get('venue', {}).get('country', 'Not Available'),
						maybe_rsvp_count=event.get('maybe_rsvp_count', 0),
						time=event.get('time', 0),
						created=event.get('created', None),
					)

	return HttpResponse(data_to_return, content_type='application/json')


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

