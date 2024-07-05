from django.shortcuts import render,HttpResponse
from .models import empDetail

# Create your views here.

def showDetail(request):
    data=empDetail.objects.all().values()
    print(data)
    return render(request,'base.html',context={'data':data})

def index(request):
    return HttpResponse("this is index page you are viewing ")
