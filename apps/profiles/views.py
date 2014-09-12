import datetime
import logging
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.cache import cache_page
import pytz
from django.utils import timezone
from apps.meetup.models import Event
from apps.profiles.forms import InterestForm, ProfileForm, GettingStartedForm, UserCityForm
from models import Interest, Profile, UserCity


logger = logging.getLogger(__name__)


def home(request):
    """Home page"""
    return render(request, 'index.html')


def login(request):
    return render(request, 'registration/login.html')


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

@login_required
def settings(request):
    """Handles new interests, notifications, and event preferences"""
    interests = Interest.objects.filter(profile=request.user)  # based on selected user only
    profile = Profile.objects.get(id=request.user.id)
    cities = UserCity.objects.filter(profile=request.user)

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

    if 'city' in request.POST:
        city_form = UserCityForm(request.POST, prefix='city')
        if city_form.is_valid():
            city = city_form.save(commit=False)
            city.profile = request.user
            city.save()
            return redirect("/settings")

    else:
        city_form = UserCityForm(prefix='city')

    data = {'user': request.user, 'interests': interests, 'profile': profile,
            'interest_form': interest_form, 'profile_form': profile_form,
            'cities': cities, 'city_form': city_form
    }
    return render(request, 'settings.html', data)


@login_required
def profile(request):
    current_time = timezone.localtime(timezone.now())

    city_event = Event.objects.filter(city=request.user.city,
                                      start_dateTime__gte=current_time).order_by('?')[:8]
    food = Event.objects.filter(city=request.user.city,
                                description__icontains='food',
                                start_dateTime__gte=current_time).order_by('last_modified')[:1]
    community = Event.objects.filter(city=request.user.city,
                                     description__icontains='community',
                                     start_dateTime__gte=current_time).order_by('last_modified')[:1]
    wellness = Event.objects.filter(city=request.user.city,
                                    description__icontains='health',
                                    start_dateTime__gte=current_time).order_by('last_modified')[:1]
    education = Event.objects.filter(city=request.user.city,
                                     description__icontains='learn',
                                     start_dateTime__gte=current_time).order_by('last_modified')[:1]
    personal = Event.objects.filter(city=request.user.city).order_by('last_modified')[:2]

    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/profile')

    data = {
        'user': request.user, 'city_event': city_event, 'food': food,
        'community': community, 'wellness': wellness, 'education': education,
        'personal': personal, 'timezones': pytz.common_timezones
    }
    return render(request, 'profiles/view_profile.html', data)


@login_required
def delete_interest(request, interest_id):
    """Delete an interest"""
    interest = Interest.objects.get(id=interest_id)
    interest.delete()
    return redirect('/settings')


@login_required
def delete_user_city(request, usercity_id):
    """Delete a city"""
    city = UserCity.objects.get(id=usercity_id)
    city.delete()
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


class TimezoneMiddleware(object):
    def process_request(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()