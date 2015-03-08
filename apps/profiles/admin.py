from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.profiles.forms import ProfileCreationForm
from apps.profiles.models import Profile, Interest, CategoryPreference, UserCity, AuthProvider

@admin.register(Profile)
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

    list_display = ['id', 'username', 'provider', 'city', 'zip_code']
    search_fields = ['username', 'provider', 'city', 'zip_code']


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['name', 'choice', 'profile']


@admin.register(UserCity)
class UserCityAdmin(admin.ModelAdmin):
    list_display = ['name', 'profile']


admin.site.register(AuthProvider)
admin.site.register(CategoryPreference)

