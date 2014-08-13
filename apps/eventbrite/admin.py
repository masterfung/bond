from django.contrib import admin

# Register your models here.
from models import EventbriteEvent, EventbriteOAuth

class EventBriteOAuthAdmin(admin.ModelAdmin):
	list_display = ['event_name', 'city', 'latitude', 'longitude']
	search_fields = ['event_name', 'city']

admin.site.register(EventbriteEvent)
admin.site.register(EventbriteOAuth, EventBriteOAuthAdmin)