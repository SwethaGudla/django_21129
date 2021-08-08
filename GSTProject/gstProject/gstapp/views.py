from django.shortcuts import render, HttpResponseRedirect
from .forms import gstregistration, SignUpForm
from django.contrib import messages
from .models import GstRegistration
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def show(request):
    if request.method == 'POST':
        fm = gstregistration(request.POST)
        if fm.is_valid():
            Invoice_Number = fm.cleaned_data['Invoice_Number']
            Date = fm.cleaned_data['Date']
            Customer_Name = fm.cleaned_data['Customer_Name']
            Customer_Address = fm.cleaned_data['Customer_Address']
            Customer_Mobile_Number = fm.cleaned_data['Customer_Mobile_Number']
            Product = fm.cleaned_data['Product']
            Product_Price = fm.cleaned_data['Product_Price']
            GST = fm.cleaned_data['GST']
            Total = Product_Price + (Product_Price * (GST / 100))
            data = GstRegistration(Invoice_Number=Invoice_Number, Date=Date, Customer_Name=Customer_Name,
                                   Customer_Address=Customer_Address,
                                   Customer_Mobile_Number=Customer_Mobile_Number
                                   , Product=Product, Product_Price=Product_Price, GST=GST, Total=Total)
            data.save()
            messages.success(request, 'Successfully')
    else:
        fm = gstregistration()
    return render(request, 'base.html', {'form': fm, 'data': GstRegistration.objects.all()})


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created successfully')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'sign_up.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged Successfully ')
                    return HttpResponseRedirect('/show/')
        else:
            fm = AuthenticationForm()
            return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/show/')


def update_data(request, id):
    if request.method == 'POST':
        pi = GstRegistration.objects.get(pk=id)
        fm = gstregistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = GstRegistration.objects.get(pk=id)
        fm = gstregistration(instance=pi)
    return render(request, 'update.html', {'form': fm})


def delete_data(request, id):
    if request.method == 'POST':
        pi = GstRegistration.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
