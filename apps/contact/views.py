# Create your views here.

from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import FormView

from bond.apps.contact.forms import ContactForm


class ContactFormView(FormView):

    form_class = ContactForm
    template_name = "contact/email_form.html"
    success_url = '/email-sent/'

    def form_valid(self, form):
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        send_mail(
            subject=form.cleaned_data.get('subject').strip(),
            message=message,
            from_email='questions@bondandme.com',
            recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],
        )
        return super(ContactFormView, self).form_valid(form)