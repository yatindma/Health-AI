from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StaffSchedule_form(forms.Form):
    # FromDate = forms.DateField()

    # ToDate = forms.DateField()
    FromDate = forms.DateField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "FromDate",                
                "class": "form-control"
            }
        ))

    ToDate = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "ToDate",                
                "class": "form-control"
            }
        ))