from crispy_forms.helper import FormHelper
from django import forms
from django.forms import ModelForm
from djangular.forms import NgFormValidationMixin, NgModelFormMixin
from apps.profiles.models import Interest, Profile


class InterestForm(ModelForm):
	class Meta:
		model = Interest
		exclude = ['profile']


class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['first_name', 'last_name', 'email', 'email_notification', 'text_notification']


class GettingStartedForm(forms.Form):
	choices = (
		(3, "Strongly Agree"),
		(2, "Agree"),
		(1, "Disagree"),
		(0, "Strongly Disagree"),
	)

	timeline = (
		(3, "More than 4 years"),
		(2, "2 to 4 years"),
		(1, "6 months to 2 years"),
		(0, "Less than 1 year"),
	)

	negative_questions = (
		(0, "Strongly Agree"),
		(1, "Agree"),
		(2, "Disagree"),
		(3, "Strongly Disagree"),
	)

	negative_answers = (
		(0, "Sell immediately"),
		(1, "Look to sell shortly"),
		(3, "Buy the dip"),
		(2, "Leave my positions alone"),
	)

	yes_no = (
		(-3, "YES"),
		(3, "NO")
	)
	pos_yes_no = (
		(3, "YES"),
		(-3, "NO")
	)

	One = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                             label="I attend food events in my community frequently")
	Two = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                             label="Physical well-being is important to me")
	Three = forms.TypedChoiceField(choices=timeline, coerce=int, widget=forms.RadioSelect,
	                               label="I am currently seeking to build a stronger community/network")
	Four = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                              label="Attending conferences, workshops, and/or talks are important to my personal growth")
	Five = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                              label="I am more likely to attend an event if my friends will partake")
	Six = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                             label="I spend most of my free time with friends and families")
	Seven = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                               label="My preferred style of learning is hands-on rather than theoretical")
	Eight = forms.TypedChoiceField(choices=negative_questions, coerce=int, widget=forms.RadioSelect,
	                               label="I enjoy planning my schedule in advance")
	Nine = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                              label="I personally enjoy participating in philanthropic events")
	Ten = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                             label="I know quite a bit about economic issues and personal investing.")
	Eleven = forms.TypedChoiceField(choices=negative_answers, coerce=int, widget=forms.RadioSelect,
	                                label="I involve myself in competitive sports")
	Twelve = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	                                label="I tend to have a lot of free time in a given week")
	Thirteen = forms.TypedChoiceField(choices=yes_no, coerce=int, widget=forms.RadioSelect,
	                                  label="I enjoy trying risk and trying new things")
	# Fourteen = forms.TypedChoiceField(choices=pos_yes_no, coerce=int, widget=forms.RadioSelect,
	# label="Do you believe that interest rates relate to the performance of investments")
	# Fifteen = forms.TypedChoiceField(choices=pos_yes_no, coerce=int, widget=forms.RadioSelect,
	# label="If one investment had expected returns of 20% but could easily "
	#                                        "have returns of -20%, would you invest in that?")
	# Sixteen = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
	#                                  label="I would prefer to invest in a well diversified portfolio that spreads"
	#                                        " my investment across the major asset classes and understand that "
	#                                        "this may reduce the potential returns although should help to lower "
	#                                        "the risk profile:")
	helper = FormHelper()
