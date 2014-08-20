from django.contrib import admin
from apps.profiles.models import Profile, Interest, CategoryPreference, UserCity


class ProfileAdmin(admin.ModelAdmin):
	list_display = ['username', 'provider', 'city', 'zip']
	search_fields = ['username', 'provider', 'city']

class InterestAdmin(admin.ModelAdmin):
	list_display = ['name', 'choice', 'profile']

class UserCityAdmin(admin.ModelAdmin):
	list_display = ['name', 'profile']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(CategoryPreference)
admin.site.register(UserCity, UserCityAdmin)

