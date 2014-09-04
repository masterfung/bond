__author__ = '@masterfung'

import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "test",
        "USER": os.environ.get('PG_USER'),
        "PASSWORD": os.environ.get('PG_PASSWORD'),
        "HOST": "localhost",
        "PORT": "",
    }
}