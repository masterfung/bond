from django.conf.urls import patterns, include, url
from django.contrib import admin
# from bond.meetup.views import EventDetail, EventList
from rest_framework.urlpatterns import format_suffix_patterns


admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'bond.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),

                       # url(r'^api/meetups/$', EventList.as_view(), name='event_list'),
                       # url(r'^api/meetups/(?P<pk>[0-9]+)/$', EventDetail.as_view(), name='event_detail'),

                       (r'^accounts/', include('registration.backends.default.urls')),
                       # added login and reset password to defaults

                       url('', include('social.apps.django_app.urls', namespace='social')),

                       url(r'^$', "apps.profiles.views.home", name="home"),
                       url(r'^about/$', 'apps.profiles.views.about', name='about'),
                       url(r'^why_us/$', 'apps.profiles.views.whyus', name='whyus'),

                       # url(r'^contact/$', 'contact.views.ContactFormView', name='contact'),

                       url(r'^profile/$', 'apps.profiles.views.profile', name='profile'),


                       # url(r'^profile/delete_interest/$', 'profiles.views.delete_interest', name='delete_interest'),
                       url(r'^getting_started/$', 'apps.profiles.views.getting_started', name='getting_started'),

                       url(r'^settings/$', 'apps.profiles.views.settings', name='settings'),
                       url(r'^settings/(?P<interest_id>\w+)/delete/$', 'apps.profiles.views.delete_interest',
                           name='delete_interest'),
                       # url(r'^settings/(?P<usernotification_id>\w+)/update/$', 'apps.profiles.views.update_notification', name='update_notification'),

                       # url(r'^meetup_all/$', 'meetup.tasks.meetup_api_find_open_events', name='all_open_event'),

                       url(r'^meetup_oauth/$', 'apps.meetup.views.meetup_oauth_connect', name='all_open_event'),

                       # url(r'^eventbrite_all/$', 'eventbrite.views.eventbrite', name='all_eventbrite_event'),
                       url(r'^eventbrite_all/$', 'apps.eventbrite.views.eventbriteOAuth', name='all_eventbrite_event'),

                       url(r'^events/$', 'apps.events.views.events', name='events'),

                       url(r'^event_maps/$', 'apps.maps.views.event_maps', name='event_maps'),

                       url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
                       url(r'^logout/$', 'apps.profiles.views.logout', name='logout'),

                       url(r'^a/$', 'apps.profiles.views.angular', name='angular'),

                       url(r'^search/$', include('haystack.urls')),  # pulls urls from the haystack app
                       # url(r'^search/$', 'meetup.views.search_titles', name='search'),

)

urlpatterns = format_suffix_patterns(urlpatterns)