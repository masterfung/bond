from django.forms import ModelForm
from djangular.forms import NgFormValidationMixin, NgModelFormMixin
from apps.profiles.models import Interest, UserNotification, UserEventPersonalization


class InterestForm(ModelForm):
	class Meta:
		model = Interest
		exclude = ['profile']

class UserNotificationForm(ModelForm):
	class Meta:
		model = UserNotification
		exclude = ['profile']

class UserEventPersonalizationForm(ModelForm):
	class Meta:
		model = UserEventPersonalization
		exclude = ['profile']