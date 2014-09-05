# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20140904_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(default='00000', max_length=5, blank=True),
            preserve_default=False,
        ),
    ]
