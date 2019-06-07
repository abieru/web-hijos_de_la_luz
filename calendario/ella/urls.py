from django.urls import path
from . import views

urlpatterns = [
	path('', views.ella, name='ella'),
	path('ella_gallery/', views.ella_gallery, name='ella_gallery'),
	path('espacio_sideral/', views.espacio_sideral, name='espacio_sideral'),
	path('sistema_solar/', views.sistema_solar, name='sistema_solar'),
	path('mujer_unipolar/', views.mujer_unipolar, name='mujer_unipolar'),
	path('mujer_bipolar/', views.mujer_bipolar, name='mujer_bipolar'),
	path('hombre_unipolar/', views.hombre_unipolar, name='hombre_unipolar'),
	path('hombre_bipolar', views.hombre_bipolar, name='hombre_bipolar'),
	
]
