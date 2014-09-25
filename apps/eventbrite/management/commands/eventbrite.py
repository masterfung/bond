from json import dumps
import json
import logging
import dateutil.parser
from django.utils.html import strip_tags
from requests import get
from apps.meetup.models import Event
from django.conf import settings

__author__ = '@masterfung'

from django.core.management.base import BaseCommand


logger = logging.getLogger(__name__)


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
             "jacksonville", "charlotte", "milwaukee",
             "portland"
        ]
        while page < 50:
            for city in cities:
                print page
                page += 1
                print page
                resp = get('https://www.eventbriteapi.com/v3/events/search/?',
                           params={
                               "token": settings.EVENTBRITE_OAUTH_KEY,
                               "venue.city": city,
                               "page": page,
                           }
                )

                if resp.status_code != 200:
                    print "error", resp.status_code
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
                    try:
                        datetime_start = dateutil.parser.parse(event['start']['utc'])
                        datetime_end = dateutil.parser.parse(event['end']['utc'])
                        description_info = strip_tags(event.get('description', {}))

                        eventbrite = Event.objects.update_or_create(
                            event_id=event.get('id'),

                            defaults={'source': 'Eventbrite',
                                      'description': description_info.get('text', 'Not Available'),
                                      'event_name': event.get('name', {}).get('text'),
                                      'event_url': event.get('url', None),
                                      'status': event.get('status', 'Not Available'),
                                      'event_logo':event.get('logo_url', 'Not Available'),
                                      'event_capacity':event.get('capacity', 0),
                                      'organizer_description':event.get('description', {}).get('text', 'Not Available'),

                                      'venue': event.get('venue', {}),
                                      'venue_name': event.get('venue', {}).get('name', 'Not Available'),
                                      'event_address': event.get('venue', {}).get('address', {}).get('address_1', 'Not Available'),
                                      'city': event.get('venue', {}).get('address', {}).get('city', 'Not Available'),
                                      'country': event.get('venue', {}).get('address', {}).get('country', 'Not Available'),
                                      'zip': event.get('venue', {}).get('address', {}).get('postal_code', 0),
                                      'state': event.get('venue', {}).get('address', {}).get('region', 'Not Available'),
                                      'lat': event.get('venue', {}).get('latitude', 0),
                                      'lon': event.get('venue', {}).get('longitude', 0),

                                      'ticket_classes': event.get('ticket_classes', {}),
                                      # 'start_time': formatted_start_time,
                                      # 'end_time': formatted_end_time,
                                      'start_dateTime': datetime_start,
                                      'end_dateTime': datetime_end,
                                      },

            #                 # ticket_free=event.get('ticket_classes', {}).get('fee', 'Not Available'),
            #                 # cost=event['ticket_classes'].get('cost', {}).get('display', 'Not Available'),
            #                 # cost_currency=event.get('ticket_classes', {}).get('cost', {}).get('currency', 'Not Available'),
            #                 # event_status=event.get('status', 'Not Available')
                        )
                    except:
                        logger.error('Eventbrite error')
                        # logger.error('{} from Eventbrite with index of {}'.format(event, x))
                        # logger.error('The city was: {}'.format(city))
                        # logger.debug(event)