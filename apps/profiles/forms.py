from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from djangular.forms import NgFormValidationMixin, NgModelFormMixin
from apps.profiles.models import Interest, Profile, UserCity


class ProfileCreationForm(UserCreationForm):  # 4b (whole class / module)
	'''
   A form that we can use to create a patron with no privileges

   Use this form to create user simply by admin settings through the use of username & password
   '''
	# Thanks to http://stackoverflow.com/questions/16953302/ for the solution to this one
	def clean_username(self):
		# Since User.username is unique, this check is redundant,
		# but it sets a nicer error message than the ORM. See #13147.
		username = self.cleaned_data["username"]
		try:
			Profile._default_manager.get(username=username)
		except Profile.DoesNotExist:
			return username
		raise forms.ValidationError(
			self.error_messages['duplicate_username'],
			code='duplicate_username',
		)

	class Meta(UserCreationForm.Meta):
		model = get_user_model()  # 4b


class InterestForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(InterestForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Interest
		exclude = ['profile']


class ProfileForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Profile
		fields = ['first_name', 'last_name', 'email', 'phone', 'city',
		          'email_notification', 'text_notification', 'zip',
		          'distance', 'notice_frequency']


class UserCityForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(UserCityForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = UserCity
		exclude = ['profile']


class GettingStartedForm(forms.Form):
	choices = (
		(3, "Strongly Agree"),
		(2, "Agree"),
		(1, "Disagree"),
		(0, "Strongly Disagree"),
	)

	One = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                             label="I attend food events in my community frequently")
	Two = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                             label="Physical well-being is important to me")
	Three = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                               label="I am currently seeking to build a stronger community/network")
	Four = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                              label="Attending conferences, workshops, and/or talks are important to my personal growth")
	Five = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                              label="I am more likely to attend an event if my friends will partake")
	Six = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                             label="I spend most of my free time with friends and families")
	Seven = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                               label="My preferred style of learning is hands-on rather than theoretical")
	Eight = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                               label="I enjoy planning my schedule in advance")
	Nine = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                              label="I personally enjoy participating in philanthropic events")
	Ten = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                             label="I know quite a bit about economic issues and personal investing.")
	Eleven = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                                label="I involve myself in competitive sports")
	Twelve = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                                label="I tend to have a lot of free time in a given week")

	helper = FormHelper()
