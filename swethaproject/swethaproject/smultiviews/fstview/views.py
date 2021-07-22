from django.shortcuts import render,HttpResponse

# Create your views here.
def mutli(request):
    return HttpResponse('''<p style='color:red'>django web development</p>''')

def mutlisec(request):
    return HttpResponse('''<p style='color:blue'>django web framework</p>''')