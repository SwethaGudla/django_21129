
from django.shortcuts import render,HttpResponse

# Create your views here.
def mapp(request):
    return HttpResponse('''<h1>hello m1app django</h1>''')
