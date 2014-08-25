__author__ = '@masterfung'

from rest_framework import serializers

from apps.meetup.models import Event


class TopicEventSerializer(serializers.ModelSerializer):
	# owner = serializers.Field(source='owner.username')
	# pk = serializers.Field()
	# name = serializers.CharField(max_length=200)
	# description = serializers.CharField(max_length=100000)
	# address = serializers.CharField(max_length=200)
	# city = serializers.CharField(max_length=50)
	# zip = serializers.CharField(max_length=10)
	# country = serializers.CharField(max_length=3)
	# rsvp_limit = serializers.IntegerField(max_value=10000000000)
	# status = serializers.CharField(max_length=30)
	# visibility = serializers.CharField(max_length=35)
	# venue = serializers.CharField(max_length=100000)
	# event_id = serializers.CharField(max_length=15)
	# maybe_rsvp_count = serializers.IntegerField(max_value=10000000)
	# event_url = serializers.CharField(max_length=100000)
	# duration = serializers.IntegerField(max_value=10000000)
	# utc_offset = serializers.IntegerField(max_value=100000000)
	# lat = serializers.FloatField()
	# long = serializers.FloatField()
	# how_to_find_us = serializers.CharField(max_length=1000000)
	# updated = serializers.IntegerField(max_value=1000000000)
	# group = serializers.CharField(max_length=1000000)
	# time = serializers.IntegerField(max_value=100000000)
	# created = serializers.IntegerField(max_value=100000000)
	# venue = serializers.RelatedField(many=True)
	# group = serializers.RelatedField(many=True)
	#
	#
	# def restore_object(self, attrs, instance=None):
	# 	if instance is not None:
	# 		instance.name = attrs.get('name', instance.name)


	class Meta:
		model = Event
		fields = (
			'event_name',
			'group_name',
			'description',
			'event_address',
			'city',
			'state',
			'zip',
			'country',
			'rsvp_limit',
			'status',
			'visibility',
			'venue',
			'event_id',
			'maybe_rsvp_count',
			'event_url',
			'duration',
			'utc_offset',
			'lat',
			'lon',
			'event_updated',
			'group',

		)