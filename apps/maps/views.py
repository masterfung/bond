from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from apps.meetup.models import Event


def event_maps(request):
    return render(request, 'maps/index.html')


def get_events(request):
    events = Event.objects.filter(city=request.user.city).exclude(lat=None, lon=None).order_by('?')[:10]
    response = serializers.serialize('json', events, use_natural_keys=True)
    return HttpResponse(response, content_type="application/json")