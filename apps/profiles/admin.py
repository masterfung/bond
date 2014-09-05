from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.profiles.forms import ProfileCreationForm
from apps.profiles.models import Profile, Interest, CategoryPreference, UserCity, AuthProvider


class ProfileAdmin(UserAdmin):
    add_form = ProfileCreationForm

    def get_fieldsets(self, request, obj=None):  # 4c (whole method)
        """
        Get the custom fields that are missing from the usercreationform for the PatronAdmin

        """

        return self.fieldsets + (
            ('Custom Fields', {'fields': ('provider', 'raw',
                                          'fib', 'phone', 'city',
                                          'birthday', 'zip_code', 'picture_url',
                                          'profile_updated_time', 'distance', 'email_notification',
                                          'text_notification', 'notice_frequency', 'food_score',
                                          'wellness_score', 'community_score', 'personal_score',
                                          'education_score'
            )}),
        )

    list_display = ['username', 'provider', 'city', 'zip_code']
    search_fields = ['username', 'provider', 'city']


class InterestAdmin(admin.ModelAdmin):
    list_display = ['name', 'choice', 'profile']


class UserCityAdmin(admin.ModelAdmin):
    list_display = ['name', 'profile']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(AuthProvider)
admin.site.register(Interest, InterestAdmin)
admin.site.register(CategoryPreference)
admin.site.register(UserCity, UserCityAdmin)

