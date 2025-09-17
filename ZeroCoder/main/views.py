from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'main/index.html', {'caption':"CatDjango"})

def new(request):
    return render(request, 'main/new.html')