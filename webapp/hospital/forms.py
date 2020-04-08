from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StaffSchedule_form(forms.Form):
    FromDate = forms.DateField()

    ToDate = forms.DateField()
