from django.shortcuts import render
from .forms import studentRegister

# Create your views here.
def showinfo(request):
    fm=studentRegister()
    print(fm)
    return render(request,'home.html',{'form':'abrar'})