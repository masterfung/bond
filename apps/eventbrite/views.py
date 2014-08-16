from json import dumps
import json

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from requests import get
from apps.eventbrite.models import EventbriteOAuth
from settings import local

EVENTBRITE_API_KEY = local.EVENTBRITE_API_KEY

EVENTBRITE_OAUTH_KEY = local.EVENTBRITE_OAUTH_KEY


@login_required
@user_passes_test(lambda u: u.is_superuser)
def eventbriteOAuth(request):
	page = 0
	data_to_return = []
	cities = ['san+francisco', 'boston', 'new+york', 'dallas', 'houston',
			'los+angeles', 'baltimore']
	while page < 50:
		page += 1
		resp = get('https://www.eventbriteapi.com/v3/events/search/?',
			params={
				"token": EVENTBRITE_OAUTH_KEY,
				"venue.city": "san+francisco",  # "page_count": 45,  # "page_number": 1,  # "page_size": 50,
				# "object_count": 6,
				"page": page,
			}
		)

		if resp.status_code != 200:
			print "error"
			return

		data = dumps(resp.json(), indent=2, sort_keys=True)
		data_to_return.append(data)

		events = json.loads(data)

		events = events['events']

		x = 0
		while x <= 50:
			x += 1

			if not (len(events) > x):
				break

			event = events[x]
			if event.get('venue'):
				eventbrite = EventbriteOAuth.objects.get_or_create(
					event_name=event.get('name', {}).get('text'),
					event_description=event.get('description', {}).get('text', 'Not Available'),
					event_url=event.get('url', None),
					event_id=event.get('id', 0),
					event_status=event.get('status', 'Not Available'),
					event_logo=event.get('logo_url', 'Not Available'),
					event_capacity=event.get('capacity', 0),
					created=event.get('created', 'Not Available'),
					organizer_description=event.get('description', {}).get('text', 'Not Available'),

					venue=event.get('venue', {}),
					address=event.get('venue', {}).get('address', {}).get('address_1', 'Not Available'),
					city=event.get('venue', {}).get('address', {}).get('city', 'Not Available'),
					country=event.get('venue', {}).get('address', {}).get('country', 'Not Available'),
					postal_code=event.get('venue', {}).get('address', {}).get('postal_code', 0),
					region=event.get('venue', {}).get('address', {}).get('region', 'Not Available'),
					latitude=event.get('venue', {}).get('latitude', 0),
					longitude=event.get('venue', {}).get('longitude', 0),

					ticket_classes=event.get('ticket_classes', {}),
					# ticket_free=event.get('ticket_classes', {}).get('fee', {}),
					#cost=event['ticket_classes'].get('cost', {}).get('display', 'Not Available'),
					# cost_currency=event.get('ticket_classes', {}).get('cost', {}).get('currency', 'Not Available'),
					#event_status=event.get('status', 'Not Available')
				)

	return HttpResponse(data_to_return, content_type='application.json')


# @login_required
# def eventbrite(request):
# page = 1
# 	data_to_return = []
# 	while page < 50:
# 		page += 2
# 		resp = get('https://developer.eventbrite.com/json/event_search?',
# 			params={
# 				"app_key": eventbriteApiKey,
# 				"city": "san+francisco",
# 				# "object_count": 6,
# 				"page": page,
# 			}
# 		)
# 		if resp.status_code != 200:
# 			print "error"
# 			return
#
# 		data = dumps(resp.json(), indent=2, sort_keys=True)
# 		data_to_return.append(data)
#
# 		events = json.loads(data)
# 		print events
#
# 		print 'happy'
# 		events = events['contents']['events']
# 		print events[2]['event']['id']
#
#
#
# 		x = 1
# 		while x <= 10:
# 			filtered_event = {}
# 			unfiltered_event = events[x]['event']
# 			for event in unfiltered_event.keys():
# 				if event is not None:
# 					filtered_event[event] = unfiltered_event[event]
# 			print filtered_event
# 			# events = events[x]['event']
# 			print 'hi'
# 			# events = events[x]
# 			# print events[x]['event']['organizer']['url']
# 			print events[x]['event']['description']
# 			x += 1
# 			print x
# 			# if events[x]['event']:
# 			# if events[x]['event'].get('venue') and events[x]['event'].get('tickets') and events[x]['event'].get('organizer'):
#
# 			eventbrite = EventbriteEvent.objects.get_or_create(
# 				description=filtered_event['description'],
# 				event_title=filtered_event['title'],
# 				privacy=filtered_event['privacy'],
# 				timezone=filtered_event['timezone'],
# 				timezone_offset=filtered_event['timezone_offset'],
# 				event_url=filtered_event['url'],
# 				event_start_date=filtered_event['start_date'],
# 				repeats=filtered_event['repeats'],
# 				last_modified=filtered_event['modified'],
# 				venue=filtered_event['venue'],
# 				latitude=filtered_event['venue']['latitude'],
# 				longitude=filtered_event['venue']['longitude'],
# 				address=filtered_event['venue']['address'],
# 				city=filtered_event['venue']['city'],
# 				country=filtered_event['venue']['country'],
# 				postal_code=filtered_event['venue']['postal_code'],
# 				region=filtered_event['venue']['region'],
# 				# event_id=filtered_event['id'],
#
# 				tags=filtered_event['tags'],
#
# 				tickets=filtered_event['tickets'],
# 				status=filtered_event['status'],
#
# 				organizer=filtered_event['organizer'],
# 				organizer_description=filtered_event['organizer']['description'],
# 				organizer_url=filtered_event['organizer']['url'],
#
# 				# organizer_id=filtered_event['organizer']['id'],
# 				# organizer_name=filtered_event['organizer']['name'],
#
#
#
# 				# status=events['event'].get('status', None),
# 				# timezone=events['event'].get('timezone', None),
# 				# timezone_offset=events['event'].get('timezone_offset', None),
# 				# event_url=events['event'].get('url', None),
# 				#
# 				# tags=events['event'].get('tags', 'None'),
#
# 			)
#
# 	return StreamingHttpResponse(data_to_return, content_type='application.json')

