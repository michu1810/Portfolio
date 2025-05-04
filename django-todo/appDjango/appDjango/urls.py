from django.contrib import admin
from django.urls import path, include # include pozwala podpiac apke
from ideas.views import przekieruj_na_liste


urlpatterns = [
    path('', przekieruj_na_liste),
    path('admin/', admin.site.urls),
    path('zadania/', include('ideas.urls')), # dodajemy tutaj nasza appke ideas

]

