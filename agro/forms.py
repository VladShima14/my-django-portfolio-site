from django import forms
from .models import Email

class EmailForm(forms.ModelForm):

    class Meta:
        model = Email
        fields = ('name', 'email', 'phone')

        name = forms.CharField(label='Название компании')


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    phone = forms.CharField()
    message = forms.CharField()
