from django.shortcuts import render,HttpResponse

# Create your views here.
def message(request):
    return HttpResponse('''<h1 style='color:blue;border:1px solid red'>welcome to ojas</h1>''')

def message1(request):
    return HttpResponse('''<h1 style='color:blue;border:1px solid red'>welcome to ojas</h1>''')

def message2(request):
    return HttpResponse('''<h1 style='color:blue;border:1px solid red'>welcome to ojas</h1>''')


