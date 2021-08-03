from django import forms
from .models import GstRegistration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class gstregistration(forms.ModelForm):
    class Meta:
        model = GstRegistration
        fields = ['Invoice_Number', 'Date', 'Customer_Name', 'Customer_Address', 'Customer_Mobile_Number', 'Product',
                  'Product_Price', 'GST']
        widgets = {
            'Invoice_Number': forms.TimeInput(attrs={'class': 'form-control'}),
            'Date': forms.TimeInput(attrs={'class': 'form-control'}),
            'Customer_Name': forms.TimeInput(attrs={'class': 'form-control'}),
            'Customer_Address': forms.TimeInput(attrs={'class': 'form-control'}),
            'Customer_Mobile_Number': forms.TimeInput(attrs={'class': 'form-control'}),
            'Product': forms.TimeInput(attrs={'class': 'form-control'}),
            'Product_Price': forms.TimeInput(attrs={'class': 'form-control'}),
            'GST': forms.TimeInput(attrs={'class': 'form-control'}),

        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': "Email"}
