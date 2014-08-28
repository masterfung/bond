from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.
from apps.profiles.test_utils import run_pyflakes_for_package, run_pep8_for_package


class ViewTestCase(TestCase):
    def test_home_page_image(self):
        response = self.client.get(reverse('home'))
        self.assertTrue("<img class='img-responsive img-hold' "
                      "src='https://bondandme.s3.amazonaws.com/img/second-cover.fda9e34e23a0.jpg' "
                      "alt='community bonding'/>",
                      response.content)

    def test_iubenda_privacy_policy(self):
        response = self.client.get(reverse('home'))
        self.assertTrue("<a href='//www.iubenda.com/privacy-policy/805249' "
                        "class='iubenda-nostyle no-brand iub-legal-only iubenda-embed' "
                        "title='Privacy Policy'>", response.context)

    def test_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertTrue("<title>About Us</title>", response.context)


class SyntaxTest(TestCase):
    def test_syntax(self):
        """
        Run pyflakes/pep8 across the code base to check for potential errors.
        """
        packages = ['bond']
        warnings = []
        # Eventually should use flake8 instead so we can ignore specific lines via a comment
        for package in packages:
            warnings.extend(run_pyflakes_for_package(package, extra_ignore=("_settings",)))
            warnings.extend(run_pep8_for_package(package, extra_ignore=("_settings",)))
        if warnings:
            self.fail("{0} Syntax warnings!\n\n{1}".format(len(warnings), "\n".join(warnings)))