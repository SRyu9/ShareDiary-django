from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def profilefunction(request):
    responsepbject = HttpResponse('<h1>Profile</h1>')
    return responsepbject
