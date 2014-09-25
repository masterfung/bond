from django.test import TestCase
from requests import get
from django.conf import settings


class EventbriteTest(TestCase):
    def test_api_token(self):
        response = get('https://www.eventbriteapi.com/v3/events/search/?',
            params={
                "token": settings.EVENTBRITE_OAUTH_KEY,
                "venue.city": "miami",
                "page": "1",
            }
        )
        self.assertEqual(response.status_code, 200)
