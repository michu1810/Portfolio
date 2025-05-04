from django.http import HttpResponse
from django.urls import path, include
from . import views
from django.shortcuts import redirect

def test_view(request):
	return HttpResponse("Działa!")


urlpatterns = [
	path('', lambda request: redirect('lista_ksiazek')),
	path('books/', views.lista_ksiazek, name='lista_ksiazek'),  # dodajemy tutaj nasza appke ideas
	path('dodaj/', views.dodaj_ksiazke, name='dodaj_ksiazke'),
	path('usun/<int:id>/', views.usun_ksiazke, name='usun_ksiazke'),
	path('edytuj/<int:id>/', views.edytuj_ksiazke, name='edytuj_ksiazke'),
]