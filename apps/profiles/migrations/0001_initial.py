# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('raw', models.TextField(null=True)),
                ('fib', models.BigIntegerField(null=True, blank=True)),
                ('phone', models.CharField(max_length=12, blank=True)),
                ('city', models.CharField(max_length=40, blank=True)),
                ('birthday', models.CharField(max_length=10, blank=True)),
                ('zip', models.CharField(max_length=5, blank=True)),
                ('picture_url', models.ImageField(null=True, upload_to=b'avatar/', blank=True)),
                ('profile_updated_time', models.CharField(max_length=50, blank=True)),
                ('account_created', models.DateTimeField(auto_now_add=True)),
                ('email_notification', models.CharField(default=b'Enrolled', max_length=25, choices=[(b'Enrolled', b'Enrolled'), (b'Not Enrolled', b'Not Enrolled')])),
                ('text_notification', models.CharField(default=b'Enrolled', max_length=25, choices=[(b'Enrolled', b'Enrolled'), (b'Not Enrolled', b'Not Enrolled')])),
                ('distance', models.CharField(default=b'2', max_length=20, choices=[(b'2', b'Within 2 Miles'), (b'5', b'Within 5 Miles'), (b'10', b'Within 10 Miles'), (b'20', b'Within 20 Miles'), (b'35', b'Within 35 Miles'), (b'50', b'Within 50 Miles')])),
                ('notice_frequency', models.CharField(default=b'3', max_length=20, choices=[(b'1', b'Once a week'), (b'2', b'Twice a week'), (b'3', b'Three times a week'), (b'5', b'Only on weekdays'), (b'7', b'Everyday')])),
                ('food_score', models.FloatField(default=0, null=True)),
                ('wellness_score', models.FloatField(default=0, null=True)),
                ('community_score', models.FloatField(default=0, null=True)),
                ('personal_score', models.FloatField(default=0, null=True)),
                ('education_score', models.FloatField(default=0, null=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthProvider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider', models.CharField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryPreference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('choice', models.ForeignKey(related_name=b'interest_choice', to='profiles.CategoryPreference')),
                ('profile', models.ForeignKey(related_name=b'interest_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserCity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=35)),
                ('profile', models.ForeignKey(related_name=b'usercity_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='categorypreference',
            name='choices',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='profiles.Interest'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='provider',
            field=models.ForeignKey(related_name=b'users', to='profiles.AuthProvider', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
