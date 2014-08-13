from django.db import models

# Create your models here.


class Group(models.Model):
	group_id = models.CharField(max_length=200, null=True, blank=True)
	join_mode = models.CharField(max_length=20, null=True, blank=True)
	group_name = models.CharField(max_length=200, null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	event_address = models.CharField(max_length=200, null=True, blank=True)
	city = models.CharField(max_length=50, null=True, blank=True)
	state = models.CharField(max_length=20, null=True, blank=True)
	zip = models.CharField(max_length=10, null=True, blank=True)
	country = models.CharField(max_length=30, null=True, blank=True)

	class Meta:
		abstract = True

class TopicEvent(Group):
	# owner = models.ForeignKey(AUTH_USER_MODEL, related_name='events')
	event_name = models.CharField(max_length=250, null=True, blank=True)
	rsvp_limit = models.BigIntegerField(null=True, blank=True)
	status = models.CharField(max_length=30, null=True, blank=True)
	visibility = models.CharField(max_length=35, null=True, blank=True)
	venue = models.TextField(null=True, blank=True)
	event_id = models.CharField(max_length=15, null=True, blank=True)
	maybe_rsvp_count = models.BigIntegerField(null=True, blank=True)
	event_url = models.TextField(null=True, blank=True)
	duration = models.IntegerField(max_length=10, null=True, blank=True)
	utc_offset = models.BigIntegerField(max_length=30, null=True, blank=True)
	lat = models.FloatField(max_length=30, null=True, blank=True)
	lon = models.FloatField(max_length=30, null=True, blank=True)
	how_to_find_us = models.TextField(null=True, blank=True)
	updated = models.BigIntegerField(null=True, blank=True)

	group = models.TextField(null=True, blank=True)
	time = models.BigIntegerField(null=True, blank=True)
	created = models.BigIntegerField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.event_name


