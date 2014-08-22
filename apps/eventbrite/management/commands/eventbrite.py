from json import dumps
import json
import dateutil.parser
from django.utils.html import strip_tags
from requests import get
from apps.meetup.models import Event
from settings.production import EVENTBRITE_OAUTH_KEY

__author__ = 'htm'

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        page = 0

        cities = [
            "san+francisco",
            "boston", "new+york", "houston",
            "los+angeles", "baltimore", "austin",
            "san+antonio", "nashville", "seattle", "philadelphia",
            "columbus", "dallas", "denver", "salt+lake+city",
            "las+vegas", "washington", "kansas+city",
            "minneapolis", "atlanta", "orlando", "richmond",
            "jacksonville", "charlotte", "milwaukee"
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
                        formatted_start_time = event['start']['utc'][:-1] + '-7:00'
                        formatted_end_time = event['end']['utc'][:-1] + '-7:00'
                        datetime_start = dateutil.parser.parse(event['start']['utc'])
                        datetime_end = dateutil.parser.parse(event['end']['utc'])
                        description_info = strip_tags(event.get('description', {}))
                        eventbrite = Event.objects.get_or_create(
	                        source=('Eventbrite'),
                            event_name=event.get('name', {}).get('text'),
                            description=description_info.get('text', 'Not Available'),
                            event_url=event.get('url', None),
                            event_id=event.get('id', 0),
                            status=event.get('status', 'Not Available'),
                            event_logo=event.get('logo_url', 'Not Available'),
                            event_capacity=event.get('capacity', 0),
                            organizer_description=event.get('description', {}).get('text', 'Not Available'),

                            venue=event.get('venue', {}),
                            venue_name=event.get('venue', {}).get('name', 'Not Available'),
                            event_address=event.get('venue', {}).get('address', {}).get('address_1', 'Not Available'),
                            city=event.get('venue', {}).get('address', {}).get('city', 'Not Available'),
                            country=event.get('venue', {}).get('address', {}).get('country', 'Not Available'),
                            zip=event.get('venue', {}).get('address', {}).get('postal_code', 0),
                            state=event.get('venue', {}).get('address', {}).get('region', 'Not Available'),
                            lat=event.get('venue', {}).get('latitude', 0),
                            lon=event.get('venue', {}).get('longitude', 0),

                            ticket_classes=event.get('ticket_classes', {}),
                            start_time=formatted_start_time,
                            end_time=formatted_end_time,
                            start_dateTime=datetime_start,
                            end_dateTime=datetime_end

                            # ticket_free=event.get('ticket_classes', {}).get('fee', {}),
                            # cost=event['ticket_classes'].get('cost', {}).get('display', 'Not Available'),
                            # cost_currency=event.get('ticket_classes', {}).get('cost', {}).get('currency', 'Not Available'),
                            # event_status=event.get('status', 'Not Available')
                        )