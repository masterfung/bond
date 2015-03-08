__author__ = '@masterfung'

from captcha.fields import ReCaptchaField  # Only import different from yesterday
import floppyforms as forms


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField()