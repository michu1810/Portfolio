from django.urls import path
from . import views  # importujemy nasze widoki

urlpatterns = [
    path('zadania/', views.lista_zadan, name='lista_zadan'),
    path('dodaj/', views.dodaj_zadanie, name='dodaj_zadanie'),
    path('usun/<int:id>/', views.usun_zadanie, name='usun_zadanie'),
    path('edytuj/<int:id>/', views.edytuj_zadanie, name='edytuj_zadanie'),
    path('przelacz-status/<int:id>/', views.przelacz_status_checkboxa, name='przelacz_status'),
]
