# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EventbriteEvent.description'
        db.add_column(u'eventbrite_eventbriteevent', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.event_id'
        db.add_column(u'eventbrite_eventbriteevent', 'event_id',
                      self.gf('django.db.models.fields.IntegerField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.event_title'
        db.add_column(u'eventbrite_eventbriteevent', 'event_title',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 7, 31, 0, 0), max_length=200),
                      keep_default=False)

        # Adding field 'EventbriteEvent.last_modified'
        db.add_column(u'eventbrite_eventbriteevent', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.organizer'
        db.add_column(u'eventbrite_eventbriteevent', 'organizer',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.organizer_description'
        db.add_column(u'eventbrite_eventbriteevent', 'organizer_description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.organizer_id'
        db.add_column(u'eventbrite_eventbriteevent', 'organizer_id',
                      self.gf('django.db.models.fields.IntegerField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.organizer_name'
        db.add_column(u'eventbrite_eventbriteevent', 'organizer_name',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.organizer_url'
        db.add_column(u'eventbrite_eventbriteevent', 'organizer_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.privacy'
        db.add_column(u'eventbrite_eventbriteevent', 'privacy',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.repeats'
        db.add_column(u'eventbrite_eventbriteevent', 'repeats',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.event_start_date'
        db.add_column(u'eventbrite_eventbriteevent', 'event_start_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.venue'
        db.add_column(u'eventbrite_eventbriteevent', 'venue',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.latitude'
        db.add_column(u'eventbrite_eventbriteevent', 'latitude',
                      self.gf('django.db.models.fields.IntegerField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.longitude'
        db.add_column(u'eventbrite_eventbriteevent', 'longitude',
                      self.gf('django.db.models.fields.IntegerField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.address'
        db.add_column(u'eventbrite_eventbriteevent', 'address',
                      self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.city'
        db.add_column(u'eventbrite_eventbriteevent', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.country'
        db.add_column(u'eventbrite_eventbriteevent', 'country',
                      self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.postal_code'
        db.add_column(u'eventbrite_eventbriteevent', 'postal_code',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.region'
        db.add_column(u'eventbrite_eventbriteevent', 'region',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.event_url'
        db.add_column(u'eventbrite_eventbriteevent', 'event_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.timezone'
        db.add_column(u'eventbrite_eventbriteevent', 'timezone',
                      self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.timezone_offset'
        db.add_column(u'eventbrite_eventbriteevent', 'timezone_offset',
                      self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.status'
        db.add_column(u'eventbrite_eventbriteevent', 'status',
                      self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True),
                      keep_default=False)

        # Adding field 'EventbriteEvent.tags'
        db.add_column(u'eventbrite_eventbriteevent', 'tags',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EventbriteEvent.description'
        db.delete_column(u'eventbrite_eventbriteevent', 'description')

        # Deleting field 'EventbriteEvent.event_id'
        db.delete_column(u'eventbrite_eventbriteevent', 'event_id')

        # Deleting field 'EventbriteEvent.event_title'
        db.delete_column(u'eventbrite_eventbriteevent', 'event_title')

        # Deleting field 'EventbriteEvent.last_modified'
        db.delete_column(u'eventbrite_eventbriteevent', 'last_modified')

        # Deleting field 'EventbriteEvent.organizer'
        db.delete_column(u'eventbrite_eventbriteevent', 'organizer')

        # Deleting field 'EventbriteEvent.organizer_description'
        db.delete_column(u'eventbrite_eventbriteevent', 'organizer_description')

        # Deleting field 'EventbriteEvent.organizer_id'
        db.delete_column(u'eventbrite_eventbriteevent', 'organizer_id')

        # Deleting field 'EventbriteEvent.organizer_name'
        db.delete_column(u'eventbrite_eventbriteevent', 'organizer_name')

        # Deleting field 'EventbriteEvent.organizer_url'
        db.delete_column(u'eventbrite_eventbriteevent', 'organizer_url')

        # Deleting field 'EventbriteEvent.privacy'
        db.delete_column(u'eventbrite_eventbriteevent', 'privacy')

        # Deleting field 'EventbriteEvent.repeats'
        db.delete_column(u'eventbrite_eventbriteevent', 'repeats')

        # Deleting field 'EventbriteEvent.event_start_date'
        db.delete_column(u'eventbrite_eventbriteevent', 'event_start_date')

        # Deleting field 'EventbriteEvent.venue'
        db.delete_column(u'eventbrite_eventbriteevent', 'venue')

        # Deleting field 'EventbriteEvent.latitude'
        db.delete_column(u'eventbrite_eventbriteevent', 'latitude')

        # Deleting field 'EventbriteEvent.longitude'
        db.delete_column(u'eventbrite_eventbriteevent', 'longitude')

        # Deleting field 'EventbriteEvent.address'
        db.delete_column(u'eventbrite_eventbriteevent', 'address')

        # Deleting field 'EventbriteEvent.city'
        db.delete_column(u'eventbrite_eventbriteevent', 'city')

        # Deleting field 'EventbriteEvent.country'
        db.delete_column(u'eventbrite_eventbriteevent', 'country')

        # Deleting field 'EventbriteEvent.postal_code'
        db.delete_column(u'eventbrite_eventbriteevent', 'postal_code')

        # Deleting field 'EventbriteEvent.region'
        db.delete_column(u'eventbrite_eventbriteevent', 'region')

        # Deleting field 'EventbriteEvent.event_url'
        db.delete_column(u'eventbrite_eventbriteevent', 'event_url')

        # Deleting field 'EventbriteEvent.timezone'
        db.delete_column(u'eventbrite_eventbriteevent', 'timezone')

        # Deleting field 'EventbriteEvent.timezone_offset'
        db.delete_column(u'eventbrite_eventbriteevent', 'timezone_offset')

        # Deleting field 'EventbriteEvent.status'
        db.delete_column(u'eventbrite_eventbriteevent', 'status')

        # Deleting field 'EventbriteEvent.tags'
        db.delete_column(u'eventbrite_eventbriteevent', 'tags')


    models = {
        u'eventbrite.eventbriteevent': {
            'Meta': {'object_name': 'EventbriteEvent'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'event_id': ('django.db.models.fields.IntegerField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'event_start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'event_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'event_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.IntegerField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.IntegerField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'organizer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'organizer_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'organizer_id': ('django.db.models.fields.IntegerField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'organizer_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'organizer_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'privacy': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'repeats': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'timezone_offset': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['eventbrite']