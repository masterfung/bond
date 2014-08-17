from django.contrib import admin

# Register your models here.
from search_indexes.models import Scraper

admin.site.register(Scraper)