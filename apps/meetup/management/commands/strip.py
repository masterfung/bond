from django.utils.html import strip_tags
from apps.meetup.models import TopicEvent

__author__ = 'htm'

from django.core.management.base import BaseCommand


class Command(BaseCommand):
	def handle(self, *args, **options):
		meetup = TopicEvent.objects.all()
		for event in meetup:
			event.description = strip_tags(event.description)
			event.save()