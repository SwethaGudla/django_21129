from django.shortcuts import render
from .models import student
from .forms import StudentRegister
# Create your views here.


def studentinfo(request):
    fm = StudentRegister()
    var = 25
    return render(request,"home.html",{'stu':student.objects.all() , 'fm':fm, "v":var})

def fm(request):
    return render(request,"fm.html")
