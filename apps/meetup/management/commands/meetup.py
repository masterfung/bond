from __future__ import absolute_import
import json
import datetime
import logging
from django.core.management.base import BaseCommand
from django.utils.html import strip_tags
from requests import get
import pytz
from pytz import timezone
from tzlocal import get_localzone
from dateutil.relativedelta import relativedelta
from apps.meetup.models import Event
from settings.production import MEETUP_API_KEY
# from settings.local import MEETUP_API_KEY

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        offset = 1

        locations = [
            {'city': "los angeles", 'state': "ca", 'country': "us"},
            {'city': "boston", 'state': "ma", 'country': "us"},
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
            {'city': "jacksonville", 'state': "fl", 'country': "us"},
            {'city': "austin", 'state': "tx", 'country': "us"},
            {'city': "nashville", 'state': "tn", 'country': "us"},
            {'city': "cleveland", 'state': "oh", 'country': "us"},
            {'city': "new orleans", 'state': "la", 'country': "us"},
            {'city': "milwaukee", 'state': "wi", 'country': "us"},
        ]
        print 'HIHIHI'
        while offset < 20:
            offset += 1
            timezone = get_localzone()
            print 'WOW!!!'
            for place in locations:
                resp = get("https://api.meetup.com/2/open_events.json",
                           params={
                               "key": MEETUP_API_KEY,
                               "city": place['city'],
                               "state": place['state'],
                               "country": place['country'],
                               "page": 200,
                               "radius": 50.0,
                               "offset": offset,
                           })

                if resp.status_code != 200:
                    return

                data = json.dumps(resp.json(), indent=2, sort_keys=True)
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

                    try:
                        if event.get('name') is not None:
                            counter_time = event.get('time', 0)
                            start_date_time_obj = datetime.datetime.fromtimestamp(counter_time / 1000)
                            start_date_time = timezone.localize(start_date_time_obj)
                            start_time = start_date_time.strftime('%Y-%m-%dT%H:%M:%S-07:00')
                            event_updated = event.get('updated', None)
                            event_updated_converted = datetime.datetime.fromtimestamp(event_updated / 1000)
                            created_time = event.get('created', None)
                            created_time_converted = datetime.datetime.fromtimestamp(created_time / 1000)
                            if event.get('duration', None):
                                end_time_epoch = event['time'] + event['duration']
                                end_date_time_obj = datetime.datetime.fromtimestamp(end_time_epoch / 1000)
                                end_date_time = timezone.localize(end_date_time_obj)
                                end_time = end_date_time.strftime('%Y-%m-%dT%H:%M:%S-07:00')
                            else:
                                end_date_time = start_date_time + relativedelta(hours=5)
                                end_time = end_date_time.strftime('%Y-%m-%dT%H:%M:%S-07:00')
                            meetup = Event.objects.update_or_create(
                                event_id=event.get('id', 0),

                                defaults={
                                    'source': 'Meetup',
                                    'group_id': event.get('group', {}).get('id', 'Not Available'),
                                    'join_mode': event.get('group', {}).get('join_mode', 'Not Available'),
                                    'group_name': event.get('group', {}).get('name', 'Not Available'),
                                    'event_name': event.get('name', 'Not Available'),
                                    'description': strip_tags(event.get('description', 'Not Available').strip()),
                                    'group': event.get('group', 'Not Available'),

                                    'venue': event.get('venue', 'Not Available'),
                                    'event_updated': event_updated_converted,
                                    'visibility': event.get('visibility', 'Not Available'),
                                    'status': event.get('status', 'Not Available'),
                                    'utc_offset': event.get('utc_offset', None),
                                    'rsvp_limit': event.get("rsvp_limit", 0),
                                    'event_url': event.get('event_url', 'Not Available'),
                                    'how_to_find_us': event.get('how_to_find_us', 'Not Available'),

                                    'lat': event.get('venue', {}).get('lat', 0),
                                    'lon': event.get('venue', {}).get('lon', 0),
                                    'event_address': event.get('venue', {}).get('address_1', 'Not Available'),
                                    'event_address2': event.get('venue', {}).get('address_2', 'Not Available'),
                                    'city': event.get('venue', {}).get('city', 'Not Available'),
                                    'state': event.get('venue', {}).get('state', 'Not Available'),
                                    'zip': event.get('venue', {}).get('zip', 0),
                                    'country': event.get('venue', {}).get('country', 'Not Available'),
                                    'maybe_rsvp_count': event.get('maybe_rsvp_count', 0),

                                    'start_dateTime': start_date_time,
                                    'end_dateTime': end_date_time,

                                    'event_created': created_time_converted,
                                }

                            )
                    except:
                        logger.error('Meetup error')
                        logger.error('{} from Meetup with index of {}'.format(event, x))
                        logger.error('{} city, state {}'.format(place['city'], place['state']))

