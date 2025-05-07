from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Shop.views import przekieruj_na_glowna, profile_view, checkout_view



urlpatterns = [
    path('', przekieruj_na_glowna),
    path('admin/', admin.site.urls),
    path('Shop/', include('Shop.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', profile_view, name='profile'),
    path('checkout/', checkout_view, name='checkout')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
