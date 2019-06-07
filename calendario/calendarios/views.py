from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def calendario(request):
	return render(request, "calendarios/calendarios.html")

def c2013(request):
	return render(request, 'calendarios/c2013.html')

def c2014(request):
	return render(request, 'calendarios/c2014.html')

def c2016(request):
	return render(request, 'calendarios/c2016.html')

def c2017(request):
	return render(request, 'calendarios/c2017.html')

def c2018(request):
	return render(request, 'calendarios/c2018.html')

def c2019(request):
	return render(request, 'calendarios/c2019.html')