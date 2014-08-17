from __future__ import absolute_import
from django.core.management.base import BaseCommand

from django.core.management.base import BaseCommand, CommandError
from apps.meetup.models import TopicEvent


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for poll_id in options['poll_id']:
            try:
                event = TopicEvent.objects.get(pk=poll_id)
            except TopicEvent.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            event.opened = False
            event.save()

            self.stdout.write('Successfully closed poll "%s"' % poll_id)