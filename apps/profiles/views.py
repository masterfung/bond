from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
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
	# #preferences = UserEventPersonalization.objects.filter(profile=request.user)

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
			profile.id = request.user
			profile.save()
			return redirect("/settings")
	else:
		profile_form = ProfileForm(prefix='notification', instance=profile)

	# if 'event' in request.POST:
	# 	event = UserEventPersonalizationForm(request.POST, prefix='event')
	# 	if event.is_valid():
	# 		preference = event.save(commit=False)
	# 		preference.profile = request.user
	# 		preference.save()
	# 		return redirect("/settings")
	# else:
	# 		#event = UserEventPersonalizationForm(prefix='event')

	data = {'user': request.user, 'interests': interests, 'profile': profile,
	        'interest_form': interest_form, 'profile_form': profile_form
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
	getting_started = Profile.objects.get(id=request.user.id)
	if request.method == 'POST':
		form = GettingStartedForm(request.POST)
		if form.is_valid():
			# You have so many of these fields, and probably very little else in `form.cleaned_data`
			# It would probably make more sense to loop over these fields
			picked = form.cleaned_data['One']
			picked += form.cleaned_data['Two']
			picked += form.cleaned_data['Three']
			picked += form.cleaned_data['Four']
			picked += form.cleaned_data['Five']
			picked += form.cleaned_data['Six']
			picked += form.cleaned_data['Seven']
			picked += form.cleaned_data['Eight']
			picked += form.cleaned_data['Nine']
			picked += form.cleaned_data['Ten']
			picked += form.cleaned_data['Eleven']
			picked += form.cleaned_data['Twelve']
			getting_started.risk_score = int(picked)
			getting_started.save()
			print picked
			return redirect("boot")

	else:
		form = GettingStartedForm()

	return render(request, 'getting_started.html', {'form': form})