from django.test.testcases import TestCase
from apps.utils.testing import RestfulTestMixin


class HomeTests(TestCase, RestfulTestMixin):
    view_name = 'home'

    def test_home_not_logged_in(self):
        response = self.client.get(self.reverse())
        self.assertResponseOk(response)