from django.shortcuts import render,HttpResponse

# Create your views here.
def greetings(request):
    return HttpResponse('''<h1 style='color:powder-blue;border:1px solid red'>welcome to django</h1>''')