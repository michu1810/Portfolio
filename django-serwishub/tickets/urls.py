from django.urls import path
from . import views


urlpatterns = [
	path('my-tickets/', views.ticket_list_view, name='ticket-list'),
	path('create-ticket/', views.ticket_create_view, name="create_ticket"),
	path('ticket/<int:ticket_id>/', views.ticket_detail_view, name="ticket_detail"),
	path('usun-ticket/<int:ticket_id>/', views.usun_ticket_view, name="usun_ticket"),
	path('ticket/<int:ticket_id>/status/', views.zmien_status_view, name="zmien_status"),
	path('usun-komentarz/<int:komentarz_id>/', views.usun_komentarz_view, name='usun_komentarz'),
	path('', views.ticket_list_api, name='api_ticket_list'),
	path('<int:ticket_id>/edit/', views.ticket_update_api),
	path('<int:ticket_id>/status/', views.zmien_status_api),
	path('<int:ticket_id>/assign/', views.przypisanie_ticket_api),
]
