from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    today=datetime.datetime.now()
    return render(request,'home.html',{'date':today})
