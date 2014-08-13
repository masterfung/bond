from django.contrib import admin

# Register your models here.
from models import Profile, Interest, Preference, UserNotification,\
	EventProximity, EventShare, EventFrequency,	UserEventPersonalization

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['username', 'provider', 'city', 'zip']
	search_fields = ['username', 'provider', 'city']

class InterestAdmin(admin.ModelAdmin):
	list_display = ['name', 'preference', 'profile']

class UserNotificationAdmin(admin.ModelAdmin):
	list_display = ['profile', 'email_notification', 'text_notification']

# class UserEventPersonalizationAdmin(admin.ModelAdmin):
# 	list_display = ['profile', 'event_proximity', 'email_frequency', 'event_share']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Preference)
admin.site.register(UserNotification, UserNotificationAdmin)

admin.site.register(EventProximity)
admin.site.register(EventShare)
admin.site.register(EventFrequency)
admin.site.register(UserEventPersonalization)
