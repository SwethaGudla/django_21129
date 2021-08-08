from django.shortcuts import render
from .models import Data
# Create your views here.
def home(request):
    return render(request,'home.html')
def profile(request):
    return render(request,'profile.html')
def education(request):
    return render(request,'education.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mail = request.POST.get('mail')
        message = request.POST.get('message')
        x=Data(name=name,mail=mail,message=message)
        x.save()
    return render(request,'contact.html')



