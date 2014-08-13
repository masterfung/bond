# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EventbriteEvent'
        db.create_table(u'eventbrite_eventbriteevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'eventbrite', ['EventbriteEvent'])


    def backwards(self, orm):
        # Deleting model 'EventbriteEvent'
        db.delete_table(u'eventbrite_eventbriteevent')


    models = {
        u'eventbrite.eventbriteevent': {
            'Meta': {'object_name': 'EventbriteEvent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['eventbrite']