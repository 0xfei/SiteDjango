__author__ = 'Root'
from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=20)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        words = len(message.split())
        if words < 10:
            raise forms.ValidationError('Too short too boring')
        return message
