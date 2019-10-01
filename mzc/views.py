from django.shortcuts import render
from django.http import HttpResponse
from .forms import Facultyform


# Create your views here.

def indexpage(request):
    return render(request,'index.html')


def contactpage(request):
    return render('contact.html')
def homepage(request):
    return  render('home.html') 
    def facultypage(request):
        return render(request,'faculty.html',{'form':form})
