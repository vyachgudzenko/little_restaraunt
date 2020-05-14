from django import forms

class ContactForm(forms.Form):
    required_css_class = "form-control"
    name = forms.CharField(label='Name',max_length=200)
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Subject',max_length=200)
    message = forms.CharField(label='Message',max_length=500)
