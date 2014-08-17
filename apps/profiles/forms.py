from django.forms import ModelForm
from djangular.forms import NgFormValidationMixin, NgModelFormMixin
from apps.profiles.models import Interest, Notification


class InterestForm(ModelForm):
	class Meta:
		model = Interest
		exclude = ['profile']

class NotificationForm(ModelForm):
	class Meta:
		model = Notification
		exclude = ['profile']
