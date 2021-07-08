from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def HomePage(request):
    return HttpResponse('<h1>NETFLIX CLONE</h1>')
