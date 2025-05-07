from django.urls import path
from . import views

urlpatterns = [
	path('lista/', views.lista_produktow, name='lista_produktow'),
	path('lista/<int:page>/', views.lista_produktow, name='lista_produktow'),
	path('dodaj/<int:produkt_id>/', views.dodaj_do_koszyka, name='dodaj_do_koszyka'),
	path('koszyk/', views.pokaz_koszyk, name='pokaz_koszyk'),
	path('usun/<int:produkt_id>/', views.usun_z_koszyka, name='usun_z_koszyka'),
	path('aktualizuj/<int:produkt_id>/', views.aktualizuj_koszyk, name='aktualizuj_koszyk'),
	path('szczegoly/<int:produkt_id>/', views.szczegoly_produktu, name='szczegoly_produktu'),
	path('checkout/', views.checkout_view, name='checkout'),
	path('register/', views.register_view, name='register'),
	path('accounts/profile/', views.profile_view, name='profile')

]