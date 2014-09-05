from django.conf.urls import patterns, include, url
# from bond.meetup.views import EventDetail, EventList
from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import search_view_factory, FacetedSearchView
from rest_framework import viewsets, routers
from rest_framework import permissions
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

from apps.meetup.models import Event
from apps.meetup.views import EventList, EventDetail

# ViewSets define the view behavior.
class EventViewSet(viewsets.ModelViewSet):
	permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	model = Event

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'events', EventViewSet)

# Faceting for Haystack:ES
sqs = SearchQuerySet().facet('city')

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'bond.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^bondinfinity/', include(admin.site.urls)),
                       url(r'^bondinfinity/doc', include('django.contrib.admindocs.urls')),

                       url(r'^api/events/$', EventList.as_view(), name='event_list'),
                       url(r'^api/events/(?P<pk>[0-9]+)/$', EventDetail.as_view(), name='event_detail'),

                      # (r'^accounts/', include('registration.backends.default.urls')),

                       # added login and reset password to defaults

                       url('', include('social.apps.django_app.urls', namespace='social')),

                       url(r'^$', "apps.profiles.views.home", name="home"),
                       url(r'^about/$', 'apps.profiles.views.about', name='about'),
                       url(r'^why-us/$', 'apps.profiles.views.whyus', name='whyus'),
                       url(r'^login/$', 'apps.profiles.views.login', name='login'),

                       url(r'^contact/$', 'apps.contact.views.contact', name='contact'),

                       url(r'^profile/$', 'apps.profiles.views.profile', name='profile'),

                       url(r'^getting-started/$', 'apps.profiles.views.getting_started', name='getting_started'),

                       url(r'^settings/$', 'apps.profiles.views.settings', name='settings'),
                       url(r'^settings/(?P<interest_id>\w+)/delete/$', 'apps.profiles.views.delete_interest',
                           name='delete_interest'),

                       url(r'^settings/(?P<usercity_id>\w+)/$', 'apps.profiles.views.delete_user_city',
                           name='delete_city'),
                       # url(r'^meetup_all/$', 'meetup.tasks.meetup_api_find_open_events', name='all_open_event'),

                       url(r'^meetup-oauth/$', 'apps.meetup.views.meetup_oauth_connect', name='all_open_event'),

                       # url(r'^eventbrite_all/$', 'eventbrite.views.eventbrite', name='all_eventbrite_event'),
                       # url(r'^eventbrite_all/$', 'apps.eventbrite.views.eventbriteOAuth', name='all_eventbrite_event'),

                       url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

                       url(r'^events/$', 'apps.events.views.events', name='events'),

                       url(r'^map/$', 'apps.maps.views.event_maps', name='map'),
                       url(r'^get-events/$', 'apps.maps.views.get_events', name='get_events'),

                       url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
                       url(r'^logout/$', 'apps.profiles.views.logout', name='logout'),

                       url(r'^a/$', 'apps.profiles.views.angular', name='angular'),

                       url(r'^search/$', include('haystack.urls')),

                       # pulls urls from the haystack app
                       # url(r'^search/$', 'apps.meetup.views.autocomplete', name='autocomplete'),
                       # pulls urls from the haystack app
                       url(r'^search/category/$', search_view_factory(searchqueryset=SearchQuerySet().facet('city'),
                                                                      view_class=FacetedSearchView,
                                                                      form_class=FacetedSearchForm),
                                                                      name='faceted_search'),

)

urlpatterns = format_suffix_patterns(urlpatterns)
