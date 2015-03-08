from django.contrib import admin

# Register your models here.

from models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'description', 'city', 'lat', 'lon', 'start_dateTime', 'end_dateTime']
    search_fields = ['event_name', 'event_id', 'city', 'description', 'source', 'start_dateTime']