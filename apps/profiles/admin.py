from django.contrib import admin
from apps.profiles.models import Profile, Interest, CategoryPreference


class ProfileAdmin(admin.ModelAdmin):
	list_display = ['username', 'provider', 'city', 'zip']
	search_fields = ['username', 'provider', 'city']

class InterestAdmin(admin.ModelAdmin):
	list_display = ['name', 'choice', 'profile']

# class NotificationAdmin(admin.ModelAdmin):
# 	list_display = ['profile', 'email', 'text']

# class UserEventPersonalizationAdmin(admin.ModelAdmin):
# 	list_display = ['profile', 'event_proximity', 'email_frequency', 'event_share']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(CategoryPreference)
# admin.site.register(Notification, NotificationAdmin)
#
# admin.site.register(EventProximity)

