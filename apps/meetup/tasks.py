# from settings import local

__author__ = '@masterfung'
import json
from json import dumps

from django.http import HttpResponse
from requests import get

from apps.meetup.serializer import TopicEventSerializer


# from .permissions import IsOwnerOrReadOnly

from apps.meetup.celery import app


def hello_world():
    print('Hello World')

# MEETUP_API_KEY = local.MEETUP_API_KEY
#
# def meetup_api_find_open_events(request):
#     resp = get("https://api.meetup.com/2/open_events.json",
#         params={
#             "key": MEETUP_API_KEY,
#             "city": "san francisco",
#             "state": "ca",
#             "country": "us",  # "topic": "python",
#         },
#         )
#
#     if resp.status_code != 200:
#         print "error"
#         return
#
#     data = dumps(resp.json(), indent=2, sort_keys=True)
#
#     events = json.loads(data)
#
#     events = events['results']
#     print events
    # serialized_data = TopicEventSerializer(data=events, many=True)
    # if serialized_data.is_valid():
    #     serialized_data.save()
    # else:
    #     print serialized_data.errors


    #
    # return HttpResponse(data, content_type='application/json')