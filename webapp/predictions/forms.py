# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class attack_prediction_form(forms.Form):
    """
        Creating Heart attack prediction Form model 
    """
    age = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "age",                
                "class": "form-control"
            }
        ))

    sex = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "sex",                
                "class": "form-control"
            }
        ))

    cp = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "cp",                
                "class": "form-control"
            }
        ))

    trestbps = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "trestbps",                
                "class": "form-control"
            }
        ))

    chol = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "chol",                
                "class": "form-control"
            }
        ))

    fbs = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "fbs",                
                "class": "form-control"
            }
        ))

    restecg = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "restecg",                
                "class": "form-control"
            }
        ))

    thalach = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "thalach",                
                "class": "form-control"
            }
        ))                                

    exang = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "exang",                
                "class": "form-control"
            }
        ))  

    oldpeak = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "oldpeak",                
                "class": "form-control"
            }
        ))  

    slope = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "slope",                
                "class": "form-control"
            }
        ))  

    ca = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "ca",                
                "class": "form-control"
            }
        ))  

    thal = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "thal",                
                "class": "form-control"
            }
        ))                                  




