from django.contrib import admin
from django.urls import path, include
from wydatki.views import przekieruj_na_glowna

urlpatterns = [
    path('', przekieruj_na_glowna),
    path('admin/', admin.site.urls),
    path('wydatki/', include('wydatki.urls')),  # dodajemy tutaj nasza appke ideas
]
