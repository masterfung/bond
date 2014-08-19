from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from apps.meetup.models import Event
from apps.profiles.forms import InterestForm, ProfileForm, GettingStartedForm
from models import Interest, Profile


def home(request):
	"""Home page"""
	return render(request, 'index.html')


def logout(request):
	"""Logs out user"""
	auth_logout(request)
	return redirect('/')


@cache_page(3600)
def about(request):
	"""About page"""
	return render(request, 'menu/about.html')


@cache_page(3600)
def whyus(request):
	"""Why choose us page"""
	return render(request, 'menu/why_us.html')


def angular(request):
	return render(request, 'angular.html')


def settings(request):
	"""Handles new interests, notifications, and event preferences"""
	interests = Interest.objects.filter(profile=request.user)  # based on selected user only
	profile = Profile.objects.get(id=request.user.id)
	city_event = Event.objects.filter(city=request.user.city)

	if 'interest' in request.POST:
		interest_form = InterestForm(request.POST, prefix='interest')
		if interest_form.is_valid():
			interest = interest_form.save(commit=False)
			interest.profile = request.user
			interest.save()
			return redirect("/settings")
	else:
		interest_form = InterestForm(prefix='interest')

	if 'notification' in request.POST:
		profile_form = ProfileForm(request.POST, prefix='notification', instance=request.user)
		if profile_form.is_valid():
			profile = profile_form.save(commit=False)
			profile.save()
			return redirect("/settings")
	else:
		profile_form = ProfileForm(prefix='notification', instance=profile)

	data = {'user': request.user, 'interests': interests, 'profile': profile,
	        'interest_form': interest_form, 'profile_form': profile_form,
	        'city_event': city_event
	}
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
	return render(request, "settings.html", data)


@login_required
def delete_interest(request, interest_id):
	"""Delete interest"""
	interest = Interest.objects.get(id=interest_id)
	interest.delete()
	return redirect('/settings')


@login_required
def update_profile(request, profile_id):
	profile = Profile.objects.get(id=profile_id)
	data = {'profile': profile}
	return render(request, '/settings.html', data)


@login_required()
def getting_started(request):
	survey = Profile.objects.get(id=request.user.id)
	if request.method == 'POST':
		print 'post'
		form = GettingStartedForm(request.POST)
		if form.is_valid():
			food = form.cleaned_data['One']
			wellness = form.cleaned_data['Two']
			community = form.cleaned_data['Three']
			education = form.cleaned_data['Four']
			personal = form.cleaned_data['Five']
			personal += form.cleaned_data['Six']
			personal += form.cleaned_data['Seven']
			personal += form.cleaned_data['Eight']
			community += form.cleaned_data['Nine']
			wellness += form.cleaned_data['Ten']
			personal += form.cleaned_data['Eleven']
			personal += form.cleaned_data['Twelve']

			survey.food_score = int(food)
			survey.wellness_score = int(wellness)
			survey.community_score = int(community)
			survey.education_score = int(education)
			survey.personal_score = int(personal)
			survey.save()

			return redirect("profile")

	else:
		form = GettingStartedForm()
	data = {'form': form}
	return render(request, 'getting_started.html', data)