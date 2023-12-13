from django import forms
class sentform(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField()
    subject = forms.CharField()
    message = forms.CharField(required=True)