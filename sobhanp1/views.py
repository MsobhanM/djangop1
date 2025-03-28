from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    # return HttpResponse('home!')
    return render(request , 'home.html')

def about(request):
    # return HttpResponse('hello world!')
    return render(request , 'about.html')