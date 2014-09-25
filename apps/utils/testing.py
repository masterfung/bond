import json
import urllib
from django.conf import settings
from django.core.urlresolvers import reverse
from rest_framework import status
from django.core import mail
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class ForceUserAuthMixin(object):
    """
        Convenience mixin that provides two methods to force user authentication,
        and get the authenticated user.
    """
    username = 'jh'

    def login_user(self, username=None):
        user = self.get_auth_user(username)
        self.client.force_authenticate(user=user)
        return user

    def get_auth_user(self, username=None):
        return User.objects.get(username=username or self.username)


class RestfulTestMixin(object):
    """
        Convenience mixin that makes testing restful/json responses much easier.
    """
    method_verbs = ['get', 'post', 'put', 'patch', 'head', 'delete']
    view_name = None
    default_kwargs = {}

    def reverse(self, view_name=None, *args, **kwargs):
        """
            Convenience reverse method that will use the `view_name` that this class
            is inherited from.

            Also, allows for appending GET arguments via the _get keyword argument.

            :: reverse(_get=dict(foo='bar')) -> ...?foo=bar
        """

        _get = kwargs.pop('_get', None)

        defaulted_kwargs = self.default_kwargs.copy()
        defaulted_kwargs.update(kwargs)

        url = reverse(view_name or self.view_name, args=args, kwargs=defaulted_kwargs)

        if _get:
            url += '?' + urllib.urlencode(_get)

        return url

    def assertNotAuthorized(self, view_name=None, *args, **kwargs):
        """
            Asserts that the view will return 403 forbidden.
        """
        response = self.client.get(self.reverse(view_name, *args, **kwargs))
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def assertAllowOnlyMethods(self, methods, view_name=None, *args, **kwargs):
        """
            Asserts that the methods passed to this function are the only methods that are allowed
            for the given view.
        """
        url = self.reverse(view_name, *args, **kwargs)

        for method in self.method_verbs:
            method_allowed = method in methods
            response = self.client.generic(method.upper(), url)
            if method_allowed:
                self.assertNotEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED,
                                    "Method %s is supposed to be allowed but isn't" % method)
            else:
                self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED,
                                  "Method %s isn't supposed to be allowed but is." % method)

    def assertResponseCodeEquals(self, response, status_code):
        """
            Asserts that the `response.status_code` is equal to `status_code`.
        """
        self.assertEquals(response.status_code, status_code)

    def assertResponseErrorEquals(self, response, error):
        """
            Asserts that the `error` in the response JSON is equal to `error`.
        """
        response_json = json.loads(response.content)
        self.assertIn('error', response_json)
        self.assertEquals(response_json['error'], error)

    def assertResponseErrorContains(self, response, error):
        """
            Asserts that the `error` in in the response JSON contains `error`
        """
        response_json = json.loads(response.content)
        self.assertIn('error', response_json)
        self.assertIn(error, response_json['error'])

    def assertResponseOk(self, response):
        """
            Asserts that the `status_code` in `response` is 200 OK.
        """
        self.assertResponseCodeEquals(response, status.HTTP_200_OK)

    def assertResponseCreated(self, response):
        """
            Asserts that the `status_code` in `response` is 201 CREATED.
        """
        self.assertResponseCodeEquals(response, status.HTTP_201_CREATED)

    def assertResponseBadRequest(self, response):
        """
            Asserts that the `status_code` in `response` is 400 BAD REQUEST.
        """
        self.assertResponseCodeEquals(response, status.HTTP_400_BAD_REQUEST)

    def assertResponseUnauthorized(self, response):
        """
            Asserts that the `status_code` in `response` is 401 UNAUTHORIZED.
        """
        self.assertResponseCodeEquals(response, status.HTTP_401_UNAUTHORIZED)

    def assertResponseForbidden(self, response):
        """
            Asserts that the `status_code` in `response` is 403 FORBIDDEN
        """
        self.assertResponseCodeEquals(response, status.HTTP_403_FORBIDDEN)

    def assertResponseNotFound(self, response):
        """
            Asserts that the `status_code` in `response` is 404 NOT FOUND.
        """
        self.assertResponseCodeEquals(response, status.HTTP_404_NOT_FOUND)

    def assertResponseHasSuccess(self, response):
        """
            Assert that the response JSON has `{'success': True}` in it.
        """
        response_json = json.loads(response.content)
        self.assertIn('success', response_json)
        self.assertTrue(response_json['success'])

    def assertResponseKeyEquals(self, response, key, value):
        """
            Assert that the value of json.loads(response.content)[key] == value
        """
        response_json = json.loads(response.content)
        self.assertIn(key, response_json)
        self.assertEquals(response_json[key], value)

    def assertResponseHasKey(self, response, key):
        """
            Assert that the value of key in json.loads(response.content)
        """
        response_json = json.loads(response.content)
        self.assertIn(key, response_json)

    def assertResponseKeyNotEquals(self, response, key, value):
        """
            Assert that the value of json.loads(response.content)[key] != value
        """
        response_json = json.loads(response.content)
        self.assertIn(key, response_json)
        self.assertNotEquals(response_json[key], value)

    def assertResponseKeyLengthEquals(self, response, key, value):
        """
            Assert that the value of len(json.loads(response.content)[key]) == value
        """
        response_json = json.loads(response.content)
        self.assertIn(key, response_json)
        self.assertEquals(len(response_json[key]), value)

    def assertResponseDoesNotContainKey(self, response, key):
        """
            Assert that the key not in json.loads(response.content)
        """
        response_json = json.loads(response.content)
        self.assertNotIn(key, response_json)

    def assertResponseKeyGte(self, response, key, value):
        """
            Assert that json.loads(response.content)[key] >= value
        """
        response_json = json.loads(response.content)
        self.assertIn(key, response_json)
        self.assertTrue(response_json[key] >= value)

    def assertResponseKeyContains(self, response, key, value, stringify=False):
        """
            Assert that value in json.loads(response.content)[key]

            If stringify is set to True, will convert what ever is at `key` into a string first.
            Good if you are looking to see if the elements of a list contain something quickly.
        """
        response_json = json.loads(response.content)
        self.assertIn(key, response_json)
        self.assertIn(value, response_json[key] if not stringify else str(response_json[key]))

    def assertDictKeyEquals(self, dictionary, key, value):
        """
            Asserts that dictionary[key] == value.
        """
        self.assertIn(key, dictionary)
        self.assertEquals(dictionary[key], value)

    def assertDictKeyNotEquals(self, dictionary, key, value):
        """
            Asserts that dictionary[key] != value.
        """
        self.assertIn(key, dictionary)
        self.assertNotEquals(dictionary[key], value)

    def assertDictKeyLcStartswith(self, dictionary, key, value):
        """
            Asserts that dictionary[key].lower().startswith(value.lower())
        """
        self.assertIn(key, dictionary)
        self.assertTrue(dictionary[key].lower().startswith(value.lower()))

    def extractKeyFromResponseJson(self, response, key):
        """
            Returns json.loads(response.content)[key].
        """
        response_json = json.loads(response.content)
        self.assertIn(key, response_json)
        return response_json[key]


class EmailMessageMixin(object):
    def fetchMessageFromEmailOutbox(self):
        self.assertTrue(len(mail.outbox) > 0, "Outbox does not contain any messages.")
        message = mail.outbox.pop(0)
        return message

    def assertEmailOutboxSizeEquals(self, size):
        self.assertEquals(len(mail.outbox), size)

    def clearEmailOutbox(self):
        mail.outbox[:] = []


class NoAsyncMaybeTaskMixin(object):
    _old_async_tasks = None
    def patchAsyncMaybeSettings(self):
        self._old_async_tasks = settings.CELERY_RUN_MAYBE_TASKS_ASYNCHRONOUSLY
        settings.CELERY_RUN_MAYBE_TASKS_ASYNCHRONOUSLY = False

    def unpatchAsyncMaybeSettings(self):
        if self._old_async_tasks is None:
            return

        settings.CELERY_RUN_MAYBE_TASKS_ASYNCHRONOUSLY = self._old_async_tasks
        self._old_async_tasks = None