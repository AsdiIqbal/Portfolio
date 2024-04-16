from django.shortcuts import render
from django.http import HttpResponse
from .models import Features
# Create your views here.

def ServicePage(request):
    m1=Features(1,"Asad",23,"M")
    m2=Features(2,"Mohsin",25,"M")
    m1.save()
    m2.save()
    print(len(Features.objects.all().values()))
    return render(request, "services.html")