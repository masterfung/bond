__author__ = '@masterfung'
import json
from json import dumps

from django.http import HttpResponse
from requests import get

from apps.meetup.serializer import TopicEventSerializer


# from .permissions import IsOwnerOrReadOnly

from apps.meetup.celery import app

@app.task
def hello_world():
    print('Hello World')

meetup_api_key = "67f634b2a311c1b104c2c2e45d3856"

def meetup_api_find_open_events(request):
    resp = get("https://api.meetup.com/2/open_events.json",
        params={
            "key": meetup_api_key,
            "city": "san francisco",
            "state": "ca",
            "country": "us",  # "topic": "python",
        },
        )

    if resp.status_code != 200:
        print "error"
        return

    data = dumps(resp.json(), indent=2, sort_keys=True)

    events = json.loads(data)

    events = events['results']
    print events
    serialized_data = TopicEventSerializer(data=events, many=True)
    if serialized_data.is_valid():
        serialized_data.save()
    else:
        print serialized_data.errors



    return HttpResponse(data, content_type='application.json')