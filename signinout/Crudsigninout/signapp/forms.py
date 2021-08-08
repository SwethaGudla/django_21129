from django.core import validators
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MUser

class PlantsRegistration(forms.ModelForm):
    class Meta:
        model = MUser
        fields = ['batch', 'name', 'type', 'details', 'Seeds', 'quantity']
        widget = {
            'batch': {'style': 'background-color: lightgrey;'}
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': "Email"}
