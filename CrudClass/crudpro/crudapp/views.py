from django.views import View
from .models import StudentRegistration
from .forms import Details
from django.contrib import messages
from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from .forms import SignupForm
from datetime import datetime, timedelta


class MyHome(View):
    def post(self,request):
        fm = Details(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            age = fm.cleaned_data['age']
            phone = fm.cleaned_data['phone']
            email = fm.cleaned_data['email']
            branch = fm.cleaned_data['branch']
            address = fm.cleaned_data['address']
            request.session['name'] = name
            request.session['email'] = email
            request.session.set_expiry(600)
            response = render(request, 'table.html')
            response.set_signed_cookie('name', name, salt='name',
                                       expires=datetime.utcnow() + timedelta(days=2))
            obj = StudentRegistration(name=name,age=age, phone=phone, email=email, branch=branch, address=address)
            obj.save()
            return redirect('/table')
            # det = StudentRegistration.objects.all()
            # return render(request, 'home.html', {'form': fm, 'details': det})
    def get(self,request):
        fm = Details()
        det = StudentRegistration.student.all()
        return render(request,'home.html',{'form':fm,'details':det})

class delete(View):
    def get(self,request,id):
        stu = StudentRegistration.student.get(pk=id)
        stu.delete()
        return redirect('/table')

class update(View):
    def post(self,request,id):
        stu = StudentRegistration.student.get(pk=id)
        form = Details(request.POST, instance=stu)
        if form.is_valid():
            messages.success(request, 'successfully updated!')
            form.save()
            return redirect('/table')

    def get(self,request,id):
        stu = StudentRegistration.student.get(pk=id)
        form = Details(instance=stu)
        return render(request, 'home.html', {'form': form})

class table(View):
    def get(self,request):
        det = StudentRegistration.student.all()
        return render(request,'table.html',{'details':det})

#---------Validations--------

class signup(View):
    def post(self,request):
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Succesfully')
            fm.save()
        return render(request, 'signup.html', {'form': fm})
    def get(self,request):
        fm = SignupForm()
        return render(request, 'signup.html', {'form': fm})


class user_login(View):
   ''' if not request.user.is_authenticated:'''
   def post(self,request):
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/home')
        return render(request, 'user_login.html', {'form': fm})
   def get(self,request):
        fm = AuthenticationForm()
        return render(request, 'user_login.html', {'form': fm})


class first_page(View):
    def get(self,request):
        return render(request,'first_page.html')

class user_logout(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/login')

#----cookies and sessions

def getsession(request):
    name = request.session['name']
    email = request.session['email']
    # name = request.session.get('name', default = 'Guest')
    # keys = request.session.keys()
    # key = request.session.items()
    # age = request.session.setdefault('age', '36')
    request.session.modified = True
    context = {'name': name, 'email': email}
    return render(request, 'getsession.html',context )

def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'delsession.html')

def getcookie(request):
    # name = request.COOKIES.get('name','Guest')
    name = request.get_signed_cookie('name', default = 'Guest',salt = 'name')
    # name = request.COOKIES['name']
    return render(request, 'getcookie.html', {'name':name})

def delcookie(request):
    response = render(request, 'delcookie.html')
    response.delete_cookie('name')
    return response