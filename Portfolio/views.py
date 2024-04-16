from django.shortcuts import render
from django.http import HttpResponse

def Homepage(request):
    return render(request,"index.html")

def Services(request):
    return render(request,"services.html")

def About(request):
    return render(request,"about.html")

def Contact(request):
    return render(request,"contact.html")