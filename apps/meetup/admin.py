from django.contrib import admin

# Register your models here.

from models import Event

class EventAdmin(admin.ModelAdmin):
	list_display = ['event_name', 'city', 'lat', 'lon']
	search_fields = ['event_name', 'city']

admin.site.register(Event, EventAdmin)