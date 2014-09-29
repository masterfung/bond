from django.test.testcases import TestCase
from apps.utils.testing import RestfulTestMixin


class HomeTests(TestCase, RestfulTestMixin):
    view_name = 'home'

    def test_home_not_logged_in(self):
        response = self.client.get(self.reverse())
        self.assertResponseOk(response)


class AboutTests(TestCase, RestfulTestMixin):
    view_name = 'about'

    def test_about_not_present(self):
        response = self.client.get(self.reverse())
        self.assertResponseOk(response)


class WhyUsTests(TestCase, RestfulTestMixin):
    view_name = 'whyus'

    def test_whyus_not_present(self):
        response = self.client.get(self.reverse())
        self.assertResponseOk(response)


class ContactTests(TestCase, RestfulTestMixin):
    view_name = 'contact'

    def test_whyus_not_present(self):
        response = self.client.get(self.reverse())
        self.assertResponseOk(response)