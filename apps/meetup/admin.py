from django.contrib import admin

# Register your models here.

from models import Event

class EventAdmin(admin.ModelAdmin):
	list_display = ['event_name', 'description','city', 'lat', 'lon']
	search_fields = ['event_name', 'city', 'description', 'lat', 'lon']

admin.site.register(Event, EventAdmin)