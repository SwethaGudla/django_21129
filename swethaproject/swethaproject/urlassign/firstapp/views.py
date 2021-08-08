from django.shortcuts import render,HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('''<h1>'hi django'</h1>''')
