__author__ = '@masterfung'

from rest_framework import serializers
from apps.meetup.models import Event


class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = (
			'id',
			'group_id',
			'join_mode',
			'group_name',
			'event_name',
			'group_name',
			'description',
			'event_address',
			'event_address2',
			'city',
			'state',
			'zip',
			'country',
			'event_name',
			'rsvp_limit',
			'status',
			'visibility',
			'venue',
			'venue_name',
			'event_id',
			'maybe_rsvp_count',
			'event_url',
			'duration',
			'utc_offset',
			'lat',
			'lon',
			'how_to_find_us',
			'event_updated',
			'group',
			'scrapy_event_url',
			'event_url',
			'event_logo',
			'event_capacity',
			'organizer_description',
			'ticket_classes',
			'start_time',
			'end_time',
			'start_dateTime',
			'end_dateTime',
			'event_created',
		)