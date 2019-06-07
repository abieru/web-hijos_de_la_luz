from django.shortcuts import render

# Create your views here.
def ella(request):
	return render(request, 'ella/ella.html')

def ella_gallery(request):
	return render(request, 'ella/ella_gallery.html')

def espacio_sideral(request):
	return render(request, 'ella/espacio_sideral.html')

def sistema_solar(request):
	return render(request, 'ella/sistema_solar.html')

def mujer_unipolar(request):
	return render(request, 'ella/mujer_unipolar.html')

def mujer_bipolar(request):
	return render(request, 'ella/mujer_bipolar.html')

def hombre_unipolar(request):
	return render(request, 'ella/hombre_unipolar.html')

def hombre_bipolar(request):
	return render(request, 'ella/hombre_bipolar.html')