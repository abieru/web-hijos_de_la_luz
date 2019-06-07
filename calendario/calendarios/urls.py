from django.urls import path
from . import views

urlpatterns = [
	path('', views.calendario, name="calendarios"),
	path('calendar2013/', views.c2013, name="calendar2013"),
	path('calendar2014/', views.c2014, name="calendar2014"),
	path('calendar2016/', views.c2016, name="calendar2016"),
	path('calendar2017/', views.c2017, name="calendar2017"),
	path('calendar2018/', views.c2018, name="calendar2018"),
	path('calendar2019/', views.c2019, name="calendar2019"),
]


