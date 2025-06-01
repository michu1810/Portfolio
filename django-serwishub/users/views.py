from django.core.exceptions import FieldError
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import login, logout
from django.urls import reverse
from django.utils.safestring import mark_safe
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_framework_simplejwt.tokens import RefreshToken
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings
from .forms import EmailAuthenticationForm
try:
    from tickets.models import Ticket
except ImportError:
    Ticket = None
    print("!!! UWAGA: Nie udało się zaimportować modelu Ticket w main_view. Sprawdź ścieżkę importu! !!!")

def register_view(request):

	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			login_url = reverse('login')
			messages.success(request,
				mark_safe(f'✔ Konto utworzone! <a href="{login_url}" class="alert-link">Zaloguj się</a>.'))
			return redirect('register')


		else:
			return render(request, 'register.html', {'form': form})
	else:
		form = CustomUserCreationForm()
		return render(request, 'register.html', {'form':form})

def login_view(request):
	if request.method == "POST":
		form = EmailAuthenticationForm(request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			messages.success(request, "✔ Zalogowano pomyślnie.")
			return redirect('main')
	else:
		form = EmailAuthenticationForm()
	return render(request, 'login.html', {'form': form})


def main_view(request):
    storage = get_messages(request)
    retrieved_messages_list = list(storage)
    if retrieved_messages_list:
        print(f"DEBUG (GET main_view): Pobrano wiadomości: {retrieved_messages_list}")

    recent_tickets_list = []

    if request.user.is_authenticated:
        print(f"DEBUG main_view: Próba pobrania zgłoszeń dla użytkownika: {request.user.email} (ID: {request.user.id})")
        if Ticket:
            try:
                #  Admin – widzi wszystkie
                if request.user.is_superuser:
                    recent_tickets_queryset = Ticket.objects.all().order_by('-data_utworzenia')
                    print("DEBUG main_view: Admin – wyświetlam wszystkie zgłoszenia.")

                #  Pracownik – tylko przypisane do niego
                elif request.user.is_staff:
                    recent_tickets_queryset = Ticket.objects.filter(pracownik=request.user).order_by('-data_utworzenia')[:10]
                    print("DEBUG main_view: Pracownik – wyświetlam zgłoszenia przypisane do niego.")

                #  Klient – tylko swoje
                else:
                    recent_tickets_queryset = Ticket.objects.filter(uzytkownik=request.user).order_by('-data_utworzenia')[:10]
                    print("DEBUG main_view: Klient – wyświetlam swoje zgłoszenia.")

                recent_tickets_list = list(recent_tickets_queryset)

                print(f"DEBUG main_view: Liczba znalezionych zgłoszeń: {len(recent_tickets_list)}")
                if len(recent_tickets_list) > 0:
                    first_ticket_display = getattr(recent_tickets_list[0], 'tytul', f"ID: {recent_tickets_list[0].id}")
                    print(f"DEBUG main_view: Pierwsze znalezione zgłoszenie: {first_ticket_display}")

            except FieldError as e:
                print(f"!!! BŁĄD main_view: FieldError - Nazwa pola w modelu Ticket jest niepoprawna. Sprawdź model! Błąd: {e} !!!")
            except Exception as e:
                print(f"!!! BŁĄD main_view: Inny błąd podczas pobierania zgłoszeń: {e} (Typ: {type(e).__name__}) !!!")
        else:
            print("DEBUG main_view: Model Ticket nie jest dostępny (problem z importem), nie pobrano zgłoszeń.")

    context = {
        'recent_tickets': recent_tickets_list,
    }
    return render(request, 'main.html', context)

def logout_view(request):
	logout(request)
	messages.success(request, "👋 Wylogowano pomyślnie.")
	return redirect('main')

def redirect_to_main(request):
	return redirect('main')

class GoogleLoginWithJWTView(SocialLoginView):
	adapter_class = GoogleOAuth2Adapter
	client_class = OAuth2Client
	callback_url = settings.GOOGLE_CALLBACK_URL

	def get_response(self):
		response = super().get_response()
		user = self.user
		refresh = RefreshToken.for_user(user)
		response.data['refresh'] = str(refresh)
		response.data['access'] = str(refresh.access_token)
		return response