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
    fib = models.BigIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    city = models.CharField(max_length=40, blank=True)
    birthday = models.CharField(max_length=10, blank=True)
    # zip = models.CharField(max_length=5, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    picture_url = models.ImageField(upload_to='avatar/', blank=True, null=True)
    profile_updated_time = models.CharField(max_length=50, blank=True)
    account_created = models.DateTimeField(auto_now_add=True)

    ENROLLED = 'Enrolled'
    NOT_ENROLLED = 'Not Enrolled'

    STATUS = (
        (ENROLLED, 'Enrolled'),
        (NOT_ENROLLED, 'Not Enrolled')
    )

    email_notification = models.CharField(max_length=25, choices=STATUS, default=ENROLLED)
    text_notification = models.CharField(max_length=25, choices=STATUS, default=ENROLLED)

    WITHIN_2 = '2'
    WITHIN_5 = '5'
    WITHIN_10 = '10'
    WITHIN_20 = '20'
    WITHIN_35 = '35'
    WITHIN_50 = '50'

    ONCE = "1"
    TWICE = '2'
    THRICE = '3'
    WEEKDAYS = '5'
    DAILY = '7'

    PROXIMITY = (
        (WITHIN_2, 'Within 2 Miles'),
        (WITHIN_5, 'Within 5 Miles'),
        (WITHIN_10, 'Within 10 Miles'),
        (WITHIN_20, 'Within 20 Miles'),
        (WITHIN_35, 'Within 35 Miles'),
        (WITHIN_50, 'Within 50 Miles'),
    )

    FREQUENCY = (
        (ONCE, 'Once a week'),
        (TWICE, 'Twice a week'),
        (THRICE, 'Three times a week'),
        (WEEKDAYS, 'Only on weekdays'),
        (DAILY, 'Everyday'),
    )

    distance = models.CharField(max_length=20, choices=PROXIMITY, default=WITHIN_2)
    notice_frequency = models.CharField(max_length=20, choices=FREQUENCY, default=THRICE)

    food_score = models.FloatField(default=0, null=True)
    wellness_score = models.FloatField(default=0, null=True)
    community_score = models.FloatField(default=0, null=True)
    personal_score = models.FloatField(default=0, null=True)
    education_score = models.FloatField(default=0, null=True)

    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)


class CategoryPreference(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    choices = models.ManyToManyField(Profile, through='Interest')

    def __unicode__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=30)
    choice = models.ForeignKey(CategoryPreference, related_name='interest_choice')
    profile = models.ForeignKey(Profile, related_name='interest_profile')

    def __unicode__(self):
        return self.name


class UserCity(models.Model):
    name = models.CharField(max_length=35)
    profile = models.ForeignKey(Profile, related_name='usercity_profile')

    def __unicode__(self):
        return self.name
