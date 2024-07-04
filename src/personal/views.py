from django.shortcuts import render,HttpResponse

# Create your views here.

def hello(request):
    return render(request,'base.html')

def index(request):
    return HttpResponse("this is index page you are viewing ")
