from django.db import models

# Create your models here.

class Scraper(models.Model):
	name = models.CharField(max_length=200, null=True)
	url = models.URLField(null=True)
	title_content = models.CharField(max_length=200, null=True)
	description_content = models.TextField(null=True)
	meta_date_content = models.CharField(max_length=200, null=True)
	meta_event_link = models.URLField(null=True)
	meta_event_location = models.CharField(max_length=200, null=True)

	def __unicode__(self):
		return self.name