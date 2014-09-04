# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Profile.profile_updated_time'
        db.alter_column(u'profiles_profile', 'profile_updated_time', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Profile.city'
        db.alter_column(u'profiles_profile', 'city', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # Changing field 'Profile.zip'
        db.alter_column(u'profiles_profile', 'zip', self.gf('django.db.models.fields.CharField')(default='', max_length=5))

        # Changing field 'Profile.phone'
        db.alter_column(u'profiles_profile', 'phone', self.gf('django.db.models.fields.CharField')(default='', max_length=12))

        # Changing field 'Profile.birthday'
        db.alter_column(u'profiles_profile', 'birthday', self.gf('django.db.models.fields.CharField')(default='', max_length=10))

    def backwards(self, orm):

        # Changing field 'Profile.profile_updated_time'
        db.alter_column(u'profiles_profile', 'profile_updated_time', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Profile.city'
        db.alter_column(u'profiles_profile', 'city', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Profile.zip'
        db.alter_column(u'profiles_profile', 'zip', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True))

        # Changing field 'Profile.phone'
        db.alter_column(u'profiles_profile', 'phone', self.gf('django.db.models.fields.CharField')(max_length=12, null=True))

        # Changing field 'Profile.birthday'
        db.alter_column(u'profiles_profile', 'birthday', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'profiles.authprovider': {
            'Meta': {'object_name': 'AuthProvider'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'profiles.categorypreference': {
            'Meta': {'object_name': 'CategoryPreference'},
            'choices': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['profiles.Profile']", 'through': u"orm['profiles.Interest']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        },
        u'profiles.interest': {
            'Meta': {'object_name': 'Interest'},
            'choice': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interest_choice'", 'to': u"orm['profiles.CategoryPreference']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interest_profile'", 'to': u"orm['profiles.Profile']"})
        },
        u'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'account_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'community_score': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'distance': ('django.db.models.fields.CharField', [], {'default': "'2'", 'max_length': '20'}),
            'education_score': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'email_notification': ('django.db.models.fields.CharField', [], {'default': "'Enrolled'", 'max_length': '25'}),
            'fib': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'food_score': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'notice_frequency': ('django.db.models.fields.CharField', [], {'default': "'3'", 'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'personal_score': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'picture_url': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'profile_updated_time': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'users'", 'null': 'True', 'to': u"orm['profiles.AuthProvider']"}),
            'raw': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'text_notification': ('django.db.models.fields.CharField', [], {'default': "'Enrolled'", 'max_length': '25'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'wellness_score': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        u'profiles.usercity': {
            'Meta': {'object_name': 'UserCity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'usercity_profile'", 'to': u"orm['profiles.Profile']"})
        }
    }

    complete_apps = ['profiles']