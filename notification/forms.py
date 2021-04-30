from django import forms
from user.models import User
from company.models import CompanyModel
from . import models

# from django.forms import widgets


class NotificationForm(forms.Form):
    company = forms.ModelChoiceField(queryset=CompanyModel.objects.all())
    price = forms.IntegerField()
    repeat = forms.BooleanField()
    active = forms.BooleanField()
