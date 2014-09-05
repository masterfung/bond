"""
Django settings for bond project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url
import os
from django.utils.crypto import get_random_string
import djcelery
import logging

logging.basicConfig(level=logging.INFO)

SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

BASE_DIR = os.path.abspath(os.path.join(SITE_ROOT, ".."))
#
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# PROJECT_DIRECTORY = os.getcwd()

# os.environ['DJANGO_SETTINGS_MODULE'] = 'bond.settings'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get("SECRET_KEY", get_random_string(50, "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

# reCAPTCHA

RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")

# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sites',
	# 'registration',
	'apps.profiles',
	'bcrypt',
	'social.apps.django_app.default',
	'apps.meetup',
	'crispy_forms',
	'floppyforms',
	'captcha',
	'scraper',
	'apps.events',
	'apps.eventbrite',
	'rest_framework',
	'djcelery',
	'djangular',
	'whoosh',
	'haystack',
	'herokuapp',
	'storages',
	'pytz',
	'dateutil',
	'tzlocal',
	'compressor',
	'django_coverage',
	'jasmine',
	'oauth2_provider',
	'corsheaders',
	'opbeat.contrib.django',
	'newrelic'
)

MIDDLEWARE_CLASSES = (
	"django.middleware.gzip.GZipMiddleware",
	"herokuapp.middleware.CanonicalDomainMiddleware",
	"django.contrib.sessions.middleware.SessionMiddleware",
	"django.middleware.common.CommonMiddleware",
	"django.middleware.csrf.CsrfViewMiddleware",
	"django.contrib.auth.middleware.AuthenticationMiddleware",
	"django.contrib.messages.middleware.MessageMiddleware",
	"django.middleware.clickjacking.XFrameOptionsMiddleware",
	'easy_timezones.middleware.EasyTimezoneMiddleware',
	'corsheaders.middleware.CorsMiddleware',
	# 'opbeat.contrib.django.middleware.Opbeat404CatchMiddleware',
)

ROOT_URLCONF = 'bond.urls'

WSGI_APPLICATION = 'bond.wsgi.application'

GEOIP_DATABASE = 'GeoLiteCity.dat'

CORS_ORIGIN_ALLOW_ALL = True

MEETUP_API_KEY1 = os.environ.get("MEETUP_API_KEY1")
EVENTBRITE_API_KEY = os.environ.get("EVENTBRITE_API_KEY")
EVENTBRITE_OAUTH_KEY = os.environ.get("EVENTBRITE_OAUTH_KEY")

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = dict(default=dj_database_url.config(default=os.environ.get("DATABASE_URL")))

DATABASES = {
	"default": dj_database_url.config(default="postgresql://"),
}

HEROKU_APP_NAME = "bondandme"

HEROKU_BUILDPACK_URL = "https://github.com/heroku/heroku-buildpack-python.git"


# The name and domain of this site.

SITE_NAME = "Bond"

SITE_DOMAIN = "www.bondandme.com"

PREPEND_WWW = False


# Rest Framework

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'oauth2_provider.ext.rest_framework.OAuth2Authentication',
	),
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.IsAuthenticated',
	),
	'DEFAULT_THROTTLE_CLASSES': (
		'rest_framework.throttling.AnonRateThrottle',
		'rest_framework.throttling.UserRateThrottle',
	),
	'DEFAULT_THROTTLE_RATES': {
		'anon': '50/day',
		'user': '1000/day'
	},
	'PAGINATE_BY': 10,  # Default to 10
	'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
	'MAX_PAGINATE_BY': 100  # Maximum limit allowed when using `?page_size=xxx`.
}

# OAuth 2

OAUTH2_PROVIDER = {  # this is the list of available scopes
                     'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

# Security settings.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

ALLOWED_HOSTS = (
	SITE_DOMAIN,
	"bondandme.herokuapp.com",
	"bondandme.com",
	"www.bondandme.com",
)

PASSWORD_HASHERS = (
	'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
	'django.contrib.auth.hashers.BCryptPasswordHasher',
	'django.contrib.auth.hashers.PBKDF2PasswordHasher',
	'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
	'django.contrib.auth.hashers.SHA1PasswordHasher',
	'django.contrib.auth.hashers.MD5PasswordHasher',
	'django.contrib.auth.hashers.CryptPasswordHasher',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.contrib.auth.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.static",
	"django.core.context_processors.tz",
	"django.contrib.messages.context_processors.messages",

	"django.core.context_processors.request",
	'social.apps.django_app.context_processors.backends',
	'social.apps.django_app.context_processors.login_redirect',
)


# Use Amazon S3 for storage for uploaded media files.

DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"


# Use Amazon S3 and RequireJS for static files storage.

STATICFILES_STORAGE = "require_s3.storage.OptimizedCachedStaticFilesStorage"

# Amazon S3 settings.

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")

AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

AWS_AUTO_CREATE_BUCKET = True

AWS_HEADERS = {
	"Cache-Control": "public, max-age=86400",
}

AWS_S3_FILE_OVERWRITE = False

AWS_QUERYSTRING_AUTH = False

AWS_S3_SECURE_URLS = True

AWS_REDUCED_REDUNDANCY = False

AWS_IS_GZIPPED = False

STATIC_URL = "https://bondandme.s3.amazonaws.com/"


# Email settings.

EMAIL_HOST = "smtp.sendgrid.net"

EMAIL_HOST_USER = os.environ.get("SENDGRID_USERNAME")

EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_PASSWORD")

EMAIL_PORT = 25

EMAIL_USE_TLS = False

SERVER_EMAIL = u"{name} <notifications@{domain}>".format(
	name=SITE_NAME,
	domain=SITE_DOMAIN,
)

DEFAULT_FROM_EMAIL = SERVER_EMAIL

EMAIL_SUBJECT_PREFIX = "[%s] " % SITE_NAME


# Opbeat

OPBEAT = {
	"ORGANIZATION_ID": os.environ.get("ORGANIZATION_ID"),
	"APP_ID": os.environ.get("APP_ID"),
	"SECRET_TOKEN": os.environ.get("SECRET_TOKEN")
}


# Error reporting settings.  Use these to set up automatic error notifications.

ADMINS = (('Johnny Hung', 'thung@me.com'),)

MANAGERS = ()

SEND_BROKEN_LINK_EMAILS = True


# Locale settings.

TIME_ZONE = "UTC"

LANGUAGE_CODE = "en-gb"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Additional static file locations.


SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"


# Namespace for cache keys, if using a process-shared cache.

CACHE_MIDDLEWARE_KEY_PREFIX = "bond"

CACHES = {
	"default": {
		"BACKEND": "django.core.cache.backends.locmem.LocMemCache",
	},  # Long cache timeout for staticfiles, since this is used heavily by the optimizing storage.
	"staticfiles": {
		"BACKEND": "django.core.cache.backends.locmem.LocMemCache",
		"TIMEOUT": 60 * 60 * 24 * 365,
		"LOCATION": "staticfiles",
	},
}

# Social

AUTHENTICATION_BACKENDS = (
	'social.backends.open_id.OpenIdAuth',
	'social.backends.facebook.FacebookOAuth2',
	'social.backends.linkedin.LinkedinOAuth2',
	'social.backends.twitter.TwitterOAuth',
	"django.contrib.auth.backends.ModelBackend",
)

SOCIAL_AUTH_PIPELINE = (
	'social.pipeline.social_auth.social_details',
	'social.pipeline.social_auth.social_uid',
	'social.pipeline.social_auth.auth_allowed',
	'social.pipeline.social_auth.social_user',
	'social.pipeline.user.get_username',
	'social.pipeline.social_auth.associate_by_email',
	'social.pipeline.user.create_user',
	'social.pipeline.social_auth.associate_user',
	'social.pipeline.social_auth.load_extra_data',
	'social.pipeline.user.user_details',
	'apps.profiles.pipeline.user.save_profile',
)

SOCIAL_AUTH_DISCONNECT_PIPELINE = (
	'social.pipeline.disconnect.allowed_to_disconnect',
	'social.pipeline.disconnect.get_entries',
	'social.pipeline.disconnect.revoke_tokens',
	'social.pipeline.disconnect.disconnect',
)

# USER_FIELDS = ['username', 'email', 'first_name', 'last_name', 'phone', 'city', 'age', 'picture_url', 'provider']
SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email', ]
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

# Facebook

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get("SOCIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get("SOCIAL_AUTH_FACEBOOK_SECRET")
SOCIAL_AUTH_FACEBOOK_SCOPE = ['user_likes', 'email', 'user_location', 'publish_actions', 'user_birthday',
                              'user_activities', 'user_groups', 'user_interests', 'user_events', 'user_work_history',
                              'friends_location', 'friends_interests', ]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'ru_RU'}

# Celery

djcelery.setup_loader()

BROKER_URL = 'redis://localhost:6379/0'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
BROKER_TRANSPORT = 'redis'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# WHOOSH

WHOOSH_INDEX = os.path.join(BASE_DIR, 'whoosh/')

# HAYSTACK

from urlparse import urlparse

es = urlparse(os.environ.get('SEARCHBOX_URL') or 'http://127.0.0.1:9200/')

HAYSTACK_CONNECTIONS = {
	'default': {
		'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
		'URL': es.scheme + '://' + es.hostname + ':80',
		'INDEX_NAME': 'documents',
	},
}

if es.username:
	HAYSTACK_CONNECTIONS['default']['KWARGS'] = {"http_auth": es.username + ':' + es.password}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
	os.path.join(SITE_ROOT, "templates"),
)

TEMPLATE_LOADERS = (
	("django.template.loaders.cached.Loader", (
		"django.template.loaders.filesystem.Loader",
		"django.template.loaders.app_directories.Loader",
	)
	),
)

STATICFILES_DIRS = (
	os.path.join(SITE_ROOT, "static", "static"),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

AUTH_USER_MODEL = 'profiles.Profile'

LOGIN_REDIRECT_URL = 'profile'

LOGIN_URL = '/login/'

SITE_ID = 1

# Compressor

COMPRESS_ENABLED = False

COMPRESS_ROOT = os.path.join(BASE_DIR, "static")

COMPRESS_CSS_FILTERS = ['compressor.filters.cssmin.CSSMinFilter']

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'compressor.finders.CompressorFinder',
)

# Logging configuration.

LOGGING = {
	"version": 1,  # Don't throw away default loggers.
	"disable_existing_loggers": False,
	"handlers": {  # Redefine console logger to run in production.
	               "console": {
		               "level": "INFO",
		               "class": "logging.StreamHandler",
	               },
	},
	"loggers": {  # Redefine django logger to use redefined console logging.
	              "django": {
		              "handlers": ["console"],
	              }
	}
}


