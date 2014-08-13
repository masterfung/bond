from django.db import models

# Create your models here.


class EventbriteEvent(models.Model):
	description = models.TextField(null=True, blank=True)
	event_id = models.IntegerField(max_length=15, null=True, blank=True)
	event_title = models.CharField(max_length=200, null=True, blank=True)
	last_modified = models.CharField(max_length=120, null=True, blank=True)

	organizer = models.TextField(null=True, blank=True)
	organizer_description = models.TextField(null=True, blank=True)
	organizer_id = models.IntegerField(max_length=15, null=True, blank=True)
	organizer_name = models.CharField(max_length=200, null=True, blank=True)
	organizer_url = models.URLField(null=True, blank=True)

	privacy = models.CharField(max_length=15, null=True, blank=True)
	repeats = models.CharField(max_length=15, null=True, blank=True) #look at this fieldset
	event_start_date = models.CharField(max_length= 100, null=True, blank=True)

	venue = models.TextField(null=True, blank=True)
	latitude = models.FloatField(max_length=15, null=True, blank=True)
	longitude = models.FloatField(max_length=15, null=True, blank=True)
	address = models.CharField(max_length=60, null=True, blank=True)
	city = models.CharField(max_length=35, null=True, blank=True)
	country = models.CharField(max_length=35, null=True, blank=True)
	postal_code = models.CharField(max_length=15, null=True, blank=True)
	region = models.CharField(max_length=30, null=True, blank=True)

	event_url = models.URLField(null=True, blank=True)
	timezone = models.CharField(max_length=50, null=True, blank=True)
	timezone_offset = models.CharField(max_length=50, null=True, blank=True)
	status = models.CharField(max_length=35, null=True, blank=True)
	tags = models.TextField(null=True, blank=True)

	tickets = models.TextField(null=True, blank=False)

	def __unicode__(self):
		return self.event_title


class EventbriteOAuth(models.Model):
	event_name = models.CharField(max_length=1000, null=True, blank=True)
	event_description = models.TextField(null=True, blank=True)
	organizer_description = models.TextField(null=True, blank=True)
	event_id = models.BigIntegerField(null=True, blank=True)
	event_url = models.URLField(null=True, blank=True)
	event_status = models.CharField(max_length=60, null=True, blank=True)
	event_capacity = models.IntegerField(max_length=100000, null=True, blank=True)

	venue = models.TextField(null=True, blank=True)
	latitude = models.FloatField(max_length=40, null=True, blank=True)
	longitude = models.FloatField(max_length=40, null=True, blank=True)
	address = models.CharField(max_length=260, null=True, blank=True)
	city = models.CharField(max_length=85, null=True, blank=True)
	country = models.CharField(max_length=85, null=True, blank=True)
	postal_code = models.CharField(max_length=25, null=True, blank=True)
	region = models.CharField(max_length=30, null=True, blank=True)

	ticket_classes = models.TextField(null=True, blank=True)
	ticket_fee = models.CharField(max_length=30, null=True, blank=True)
	cost = models.CharField(max_length=100, null=True, blank=True)
	cost_currency = models.CharField(max_length=30, null=True, blank=True)
	cost_display = models.CharField(max_length=30, null=True, blank=True)

	category_name = models.CharField(max_length=260, null=True, blank=True)
	event_logo = models.URLField(null=True, blank=True)
	created = models.CharField(max_length=60, null=True, blank=True)

	def __unicode__(self):
		return self.event_name