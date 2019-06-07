from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'core/home.html')
	
def guardianes(request):
	return render(request, 'core/guardianes.html')




	