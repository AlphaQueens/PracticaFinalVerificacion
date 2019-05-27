from django import forms
from django.core import validators


class FormUserName(forms.Form):
    name = forms.CharField(max_length=100, label="Twitter Account Name")
