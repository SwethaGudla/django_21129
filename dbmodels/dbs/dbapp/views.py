from django.shortcuts import render
from .models import Data

# Create your views here.
def show(request):
    if request.method == "POST":
        name = request.POST.get('exampleInputEmail1')
        passwrd = request.POST.get('exampleInputPassword1')
        print(name, passwrd)
        date = Data(name=name, password=passwrd)
        date.save()
    return render(request, "home.html",{'db':Data.objects.all()})
