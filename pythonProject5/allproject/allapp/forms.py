from django import forms

class StudentRegister(forms.Form):

    name = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=20)
    pas = forms.IntegerField()
