# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Scraper'
        db.create_table(u'scraper_scraper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('title_content', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('description_content', self.gf('django.db.models.fields.TextField')(null=True)),
            ('meta_date_content', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('meta_event_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('meta_event_location', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'scraper', ['Scraper'])


    def backwards(self, orm):
        # Deleting model 'Scraper'
        db.delete_table(u'scraper_scraper')


    models = {
        u'scraper.scraper': {
            'Meta': {'object_name': 'Scraper'},
            'description_content': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_date_content': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'meta_event_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'meta_event_location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'title_content': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['scraper']