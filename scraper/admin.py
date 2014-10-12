from django.contrib import admin

# Register your models here.
from scraper.models import Scraper


@admin.register(Scraper)
class ScraperAdmin(admin.ModelAdmin):
    pass