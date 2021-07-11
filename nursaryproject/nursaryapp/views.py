from django.shortcuts import render


# Create your views here.
def fun_home(request):
    return render(request,'home.html')
def fun_plants(request):
    return render(request,'plants.html')
def fun_trees(request):
    return render(request,'trees.html')






