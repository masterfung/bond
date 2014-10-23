from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from apps.contact.forms import ContactForm
from django.shortcuts import render


def contact(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(subject, message, email, ['admin@bondandme.com', 'thung@me.com'])
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()  # An unbound form

    return render(request, 'contact/contact_form.html', {
        'form': form,
    })