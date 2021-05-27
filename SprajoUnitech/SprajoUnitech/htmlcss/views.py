from re import template

from django.shortcuts import render, HttpResponseRedirect
from .forms import htmlcss_sprajo
from .models import Sprajo
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def index(request):
    data = Sprajo.objects.all()
    return render(request, 'index.html', {'items': data})


def services(request):
    return render(request,'SERVICES.html')


def products(request):
    return render(request,'product.html')


def cooling(request):
    return render(request,'Cooling.html')


def machinary(request):
    return render(request,'Machinary.html')


def safety(request):
    return render(request,'Safety.html')









