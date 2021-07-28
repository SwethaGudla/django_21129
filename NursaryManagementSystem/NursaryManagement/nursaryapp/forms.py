from django.core import validators
from django import forms
from .models import User
class PlantsRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['batch','name','type','details','Seeds','quantity']
        widget = {
            'batch':{'style':'background-color: lightgrey;'}
        }
