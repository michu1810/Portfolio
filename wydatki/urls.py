from django.urls import path, include
from . import views
from django.shortcuts import redirect


urlpatterns = [
	path('', lambda request: redirect('lista_wydatkow')),
	path('lista/', views.lista_wydatkow, name='lista_wydatkow'),
	path('dodaj/', views.dodaj_wydatek, name='dodaj_wydatek'),
	path('usun/<int:id>/', views.usun_wydatek, name='usun_wydatek'),
	path('edytuj/<int:id>/', views.edytuj_wydatek, name='edytuj_wydatek'),
]