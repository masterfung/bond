from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from apps.profiles.forms import InterestForm, UserNotificationForm, UserEventPersonalizationForm
from models import Interest, UserNotification, UserEventPersonalization


def home(request):
	"""Home page"""
	return render(request, 'index.html')


def logout(request):
	"""Logs out user"""
	auth_logout(request)
	return redirect('/')


def about(request):
	"""About page"""
	return render(request, 'menu/about.html')


def whyus(request):
	"""Why choose us page"""
	return render(request, 'menu/why_us.html')


def angular(request):
	return render(request, 'angular.html')


def settings(request):
	"""Handles new interests, notifications, and event preferences"""
	interests = Interest.objects.filter(profile=request.user) #     based on selected user only
	notifications = UserNotification.objects.filter(profile=request.user)
	preferences = UserEventPersonalization.objects.filter(profile=request.user)

	if 'interest' in request.POST:
		interest_form = InterestForm(request.POST, prefix='interest')
		if interest_form.is_valid():
			interest = interest_form.save(commit=False)
			interest.profile = request.user
			interest.save()
			return redirect("/profile")
	else:
		interest_form = InterestForm(prefix='interest')

	if 'notification' in request.POST:
		notification_form = UserNotificationForm(request.POST, prefix='notification')
		if notification_form.is_valid():
			notification = notification_form.save(commit=False)
			notification.profile = request.user
			notification.save()
			return redirect("/profile")
	else:
		notification_form = UserNotificationForm(prefix='notification')

	if 'event' in request.POST:
		event = UserEventPersonalizationForm(request.POST, prefix='event')
		if event.is_valid():
			preference = event.save(commit=False)
			preference.profile = request.user
			preference.save()
			return redirect("/profile")
	else:
		event = UserEventPersonalizationForm(prefix='event')

	data = {'user': request.user, 'interests': interests, 'notifications': notifications,
			'interest_form': interest_form, 'notification_form': notification_form,
			'event': event}
	return render(request, 'settings.html', data)


@login_required
def profile(request):

	data = {'user': request.user}
	return render(request, 'profiles/view_profile.html', data)


@login_required
def view_interest(request, interest_id):
	"""View interests"""
	interest = Interest.objects.get(id=interest_id)
	data = {'interest': interest}
	return render(request, "profiles/view_profile.html", data)


@login_required
def delete_interest(request, interest_id):
	"""Delete interest"""
	interest = Interest.objects.get(id=interest_id)
	interest.delete()
	return redirect('/profile')