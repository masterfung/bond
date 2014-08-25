# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'EventbriteEvent'
        db.delete_table(u'eventbrite_eventbriteevent')

        # Deleting model 'EventbriteOAuth'
        db.delete_table(u'eventbrite_eventbriteoauth')


    def backwards(self, orm):
        # Adding model 'EventbriteEvent'
        db.create_table(u'eventbrite_eventbriteevent', (
            ('event_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('event_title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('timezone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('organizer', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('privacy', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('event_id', self.gf('django.db.models.fields.IntegerField')(max_length=15, null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(max_length=15, null=True, blank=True)),
            ('organizer_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tags', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('timezone_offset', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('organizer_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('tickets', self.gf('django.db.models.fields.TextField')(null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('venue', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(max_length=15, null=True, blank=True)),
            ('organizer_id', self.gf('django.db.models.fields.IntegerField')(max_length=15, null=True, blank=True)),
            ('repeats', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('event_start_date', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('organizer_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'eventbrite', ['EventbriteEvent'])

        # Adding model 'EventbriteOAuth'
        db.create_table(u'eventbrite_eventbriteoauth', (
            ('event_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('ticket_classes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cost', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('event_status', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=85, null=True, blank=True)),
            ('event_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('event_id', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('event_logo', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('cost_display', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('organizer_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cost_currency', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('ticket_fee', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('event_name', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(max_length=40, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('category_name', self.gf('django.db.models.fields.CharField')(max_length=260, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=85, null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('venue', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('event_capacity', self.gf('django.db.models.fields.IntegerField')(max_length=100000, null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(max_length=40, null=True, blank=True)),
        ))
        db.send_create_signal(u'eventbrite', ['EventbriteOAuth'])


    models = {
        
    }

    complete_apps = ['eventbrite']