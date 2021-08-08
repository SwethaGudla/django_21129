from django.shortcuts import render,HttpResponse

# Create your views here.
def fstapp(request):
    return HttpResponse('''<h1>hai hello</h1>''')
