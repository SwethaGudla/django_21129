from django import forms

class StudentRegister(forms.Form):
    name=forms.CharField(initial='mr/mrs.',max_length=70)
    email=forms.EmailField(max_length=70,help_text='text')
    pwsd=forms.CharField(max_length=70,help_text='text')
    gender=forms.ChoiceField(widget=forms.RadioSelect,choices=[('1','MALE'),('2','FEMALE')])
    checkbox=forms.CharField(widget=forms.CheckboxInput)
    DateTime=forms.DateTimeField()
    TimeInput=forms.TimeInput()
    Textarea=forms.Textarea()
    Input=forms.CharField(max_length=70)
    Select=forms.CharField(max_length=70)
    NullBoolean= forms.NullBooleanField()

    URLInput=forms.URLInput()
    HiddenInput=forms.HiddenInput()