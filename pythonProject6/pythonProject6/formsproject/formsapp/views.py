from django.shortcuts import render
from .forms import StudentRegister

# Create your views here.
def ShowformData(request):
    fm=StudentRegister()
    return render(request,'home.html',{'forms':fm})

def data(request):
    fm = request.POST.get('name')
    print(fm)
    return render(request, 'data.html', {'forms': fm})