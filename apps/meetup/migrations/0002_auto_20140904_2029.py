# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 4, 20, 29, 13, 177156)),
        ),
    ]
