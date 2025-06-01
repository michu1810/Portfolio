from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from users.views import redirect_to_main, GoogleLoginWithJWTView
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from django.views.decorators.csrf import csrf_exempt

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

google_login_view = csrf_exempt(GoogleLogin.as_view())

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('api/tickets/', include('tickets.urls')),
    path('api/users/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', redirect_to_main),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path("dj-rest-auth/google/", GoogleLoginWithJWTView.as_view(), name="google_login"),
    path('accounts/', include('allauth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
