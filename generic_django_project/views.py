__author__ = 'pridemai'
from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from models import Cars
import json

def index(request):
    return render(request, 'index.html', {'test': "my data"})

def myindex(request):
    return render(request, 'mytemplate.html', {'mytest': 'test', "mytest2": "my test data 2"})

def get_cars(request):
    if "make" in request.GET:
        car_list = Cars.objects.filter(make=request.GET['make'])
    else:
        car_list = Cars.objects.all()
    data = [{"make":x.make, "model":x.model, "year":x.year} for x in car_list]
    return HttpResponse(json.dumps(data))

