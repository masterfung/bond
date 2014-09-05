# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_zip_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='zipcode',
        ),
    ]
