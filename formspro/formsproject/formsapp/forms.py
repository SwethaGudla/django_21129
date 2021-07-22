from django import forms
class studentRegister(forms.Form):
    id=forms.IntegerField(max_value=70)
    name=forms.CharField(max_length=70)
    password=forms.IntegerField(max_value=70)