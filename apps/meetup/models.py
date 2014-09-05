from datetime import datetime
from django.db import models

# Create your models here.

class Event(models.Model):
    EVENT_SOURCE = (
        ('Eventbrite', 'Eventbrite'),
        ('Meetup', 'Meetup'),
        ('Scrapy', 'Scrapy'),
        ('Other', 'Other'),
        ('None', 'None'),

    )

    source = models.CharField(max_length=20, choices=EVENT_SOURCE, default='None')
    group_id = models.CharField(max_length=200, blank=True)
    join_mode = models.CharField(max_length=20, blank=True)
    group_name = models.CharField(max_length=400, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    description = models.TextField(null=True, blank=True)
    event_address = models.CharField(max_length=400, blank=True)
    event_address2 = models.CharField(max_length=400, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=20, blank=True)
    zip = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=30, blank=True)
    event_name = models.CharField(max_length=250, blank=True)
    rsvp_limit = models.BigIntegerField(null=True, blank=True)
    status = models.CharField(max_length=30, blank=True)
    visibility = models.CharField(max_length=35, blank=True)
    venue = models.TextField(null=True, blank=True)
    venue_name = models.TextField(null=True, blank=True)
    event_id = models.CharField(max_length=15, unique=True, null=True)
    maybe_rsvp_count = models.BigIntegerField(null=True, blank=True)
    event_url = models.TextField(null=True, blank=True)
    duration = models.IntegerField(max_length=100, null=True, blank=True)
    utc_offset = models.BigIntegerField(max_length=30, null=True, blank=True)
    lat = models.FloatField(max_length=30, null=True, blank=True)
    lon = models.FloatField(max_length=30, null=True, blank=True)
    how_to_find_us = models.TextField(null=True, blank=True)

    event_updated = models.DateTimeField(null=True, blank=True)
    scrapy_event_url = models.URLField(null=True, blank=True)

    event_logo = models.URLField(null=True, blank=True)
    event_capacity = models.IntegerField(max_length=100000, null=True, blank=True)
    organizer_description = models.TextField(null=True, blank=True)
    ticket_classes = models.TextField(null=True, blank=True)

    start_time = models.CharField(max_length=150, blank=True)
    end_time = models.CharField(max_length=150, blank=True)
    start_dateTime = models.DateTimeField(null=True, blank=True)
    end_dateTime = models.DateTimeField(null=True, blank=True)

    group = models.TextField(null=True, blank=True)
    event_created = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField(default=datetime.today())
    last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.event_name


