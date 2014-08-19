from json import dumps
import json
from requests import get
from apps.eventbrite.models import EventbriteOAuth
from settings.local import EVENTBRITE_OAUTH_KEY

__author__ = 'htm'

from django.core.management.base import BaseCommand


class Command(BaseCommand):
	def handle(self, *args, **options):
		page = 0

		cities = ["san+francisco", "boston", "new+york", "houston",
		# "los+angeles", "baltimore", "austin", "san+antonio", "nashville", "seattle", "philadelphia",
		# "columbus", "dallas", "denver", "salt+lake+city", "las+vegas", "washington", "kansas+city",
		# "minneapolis", "atlanta", "orlando", "richmond"
		]

		while page < 50:
			for city in cities:

				page += 1
				resp = get('https://www.eventbriteapi.com/v3/events/search/?',
					params={
						"token": EVENTBRITE_OAUTH_KEY,
						"venue.city": city,  # "page_count": 45,  # "page_number": 1,  # "page_size": 50,
						# "object_count": 6,
						"page": page,
					}
				)

				if resp.status_code != 200:
					print "error"
					return

				data = dumps(resp.json(), indent=2, sort_keys=True)

				events = json.loads(data)

				events = events['events']

				x = 0
				while x <= 50:
					x += 1

					if not (len(events) > x):
						break
					print x
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
							# cost=event['ticket_classes'].get('cost', {}).get('display', 'Not Available'),
							# cost_currency=event.get('ticket_classes', {}).get('cost', {}).get('currency', 'Not Available'),
							# event_status=event.get('status', 'Not Available')
						)