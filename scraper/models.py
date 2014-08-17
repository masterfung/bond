from django.db import models

# Create your models here.


class Scraper(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	url = models.URLField(null=True, blank=True)
	title_content = models.CharField(max_length=700, null=True, blank=True)
	description_content = models.TextField(null=True, blank=True)
	meta_date_content = models.CharField(max_length=200, null=True, blank=True)
	meta_event_link = models.URLField(null=True, blank=True)
	meta_event_location = models.CharField(max_length=200, null=True, blank=True)

	def __unicode__(self):
		return self.name