from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class AuthProvider(models.Model):
	provider = models.CharField(max_length=100, unique=True, blank=False)

	def __unicode__(self):
		return "{}".format(self.provider)


class Profile(AbstractUser):
	provider = models.ForeignKey(AuthProvider, null=True, related_name='users')
	raw = models.TextField(null=True)
	phone = models.CharField(max_length=12, null=True)
	city = models.CharField(max_length=40, null=True)
	birthday = models.CharField(max_length=10, null=True)
	zip = models.IntegerField(max_length=5, null=True)
	picture_url = models.ImageField(upload_to='avatar/', blank=True, null=True)
	profile_updated_time = models.CharField(max_length=50, blank=True, null=True)
	account_created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "{} {}".format(self.first_name, self.last_name)


class Preference(models.Model):
	name = models.CharField(max_length=150)
	choices = models.ManyToManyField(Profile, through='Interest')

	def __unicode__(self):
		return self.name


class Interest(models.Model):
	name = models.CharField(max_length=30)
	preference = models.ForeignKey(Preference)
	profile = models.ForeignKey(Profile)

	def __unicode__(self):
		return self.name


class UserNotification(models.Model):
	email_notification = models.BooleanField(default=True)
	text_notification = models.BooleanField(default=True)
	profile = models.ForeignKey(Profile)

	def __unicode__(self):
		return str(self.email_notification)


class EventProximity(models.Model):
	length = models.IntegerField(max_length=3)
	choices = models.ManyToManyField(Profile, through='UserEventPersonalization')

	def __unicode__(self):
		return str(self.length)


class EventFrequency(models.Model):
	length = models.IntegerField(max_length=3)
	choices = models.ManyToManyField(Profile, through='UserEventPersonalization')

	def __unicode__(self):
		return str(self.length)


class EventShare(models.Model):
	name = models.CharField(max_length=50)
	choices = models.ManyToManyField(Profile, through='UserEventPersonalization')

	def __unicode__(self):
		return self.name


class UserEventPersonalization(models.Model):
	event_proximity = models.ForeignKey(EventProximity)
	event_frequency = models.ForeignKey(EventFrequency)
	event_share = models.ForeignKey(EventShare)
	profile = models.ForeignKey(Profile)

	def __unicode__(self):
		return "{}".format(self.profile.username)