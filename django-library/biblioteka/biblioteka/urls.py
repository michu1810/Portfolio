from django.contrib import admin
from django.urls import path, include
from ksiazki.views import przekieruj_na_glowna



urlpatterns = [
    path('', przekieruj_na_glowna),
    path('admin/', admin.site.urls),
    path('books/', include('ksiazki.urls')),
]
