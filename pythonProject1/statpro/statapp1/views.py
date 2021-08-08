from django.shortcuts import render
from datetime import datetime
# Create your views here.
today=datetime.now()
def home(request):
    return render(request,'home.html')
def info(request):
    return render(request,'info.html')
def home1(request):
    return render(request,'home1.html',{'date':today})



