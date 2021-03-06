from django import forms
from .models import StudentRegistration
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Details(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields ='__all__'


class SignupForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}