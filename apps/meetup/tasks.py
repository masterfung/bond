# from settings import local

__author__ = '@masterfung'
import json
from json import dumps

from django.http import HttpResponse
from requests import get

from apps.meetup.serializer import EventSerializer


# from .permissions import IsOwnerOrReadOnly

from apps.meetup.celery import app


def hello_world():
    print('Hello World')
