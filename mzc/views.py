from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def indexpage(request):
    return render(request,"index.html")


def contactpage(request):
    return HttpResponse("contactpage")
def homepage(request):
    return  HttpResponse("welcome to my home page") 
def indexpage1(request):
    return HttpResponse("welcome to my index page")    
