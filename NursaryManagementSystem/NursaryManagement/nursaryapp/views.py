from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import User
from .forms import PlantsRegistration
# Create your views here.
def add_show(request):
    if request.method == "POST":
        fm = PlantsRegistration(request.POST)
        if fm.is_valid():
            batch = fm.cleaned_data['batch']
            name = fm.cleaned_data['name']
            type = fm.cleaned_data['type']
            details = fm.cleaned_data['details']
            Seeds = fm.cleaned_data['Seeds']
            quantity = fm.cleaned_data['quantity']
            reg=User(batch=batch,name=name,type=type,details=details,Seeds=Seeds,quantity=quantity)
            reg.save()
            fm = PlantsRegistration()
    else:
        fm = PlantsRegistration()

    return render(request,'addandshow.html',{'form':fm,'data':User.objects.all()})


def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = PlantsRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = PlantsRegistration(instance=pi)
    return render(request, 'updatedetails.html', {'form': fm})


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

