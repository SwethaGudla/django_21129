from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import MUser
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
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
            reg = MUser(batch=batch, name=name, type=type, details=details, Seeds=Seeds, quantity=quantity)
            reg.save()
            fm = PlantsRegistration()
    else:
        fm = PlantsRegistration()

    return render(request, 'addandshow.html', {'form': fm, 'data': MUser.objects.all()})


def update_data(request, id):
    if request.method == 'POST':
        pi = MUser.objects.get(pk=id)
        fm = PlantsRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = MUser.objects.get(pk=id)
        fm = PlantsRegistration(instance=pi)
    return render(request, 'updatedetails.html', {'form': fm})


def delete_data(request, id):
    if request.method == 'POST':
        pi = MUser.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created successfully')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged Successfully ')
                    return HttpResponseRedirect('/addandshow')
        else:
            fm = AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/addandshow')


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'addandshow.html', {'name': request.user})
    else:
         return HttpResponseRedirect('/login')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')


class PasswordChangedForm:
    pass


def user_chanage_password(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            return HttpResponseRedirect('/addandshow')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request,'chnagedpassword.html',{'form':fm})