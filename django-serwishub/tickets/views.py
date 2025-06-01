from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TicketForm
from .models import Ticket, Komentarz
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from .serializers import GoogleSocialLoginSerializer
from django.core.paginator import Paginator
from .filters import TicketFilter


@login_required
def ticket_create_view(request):
	if request.method == "POST":
		form = TicketForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.uzytkownik = request.user
			form.save()
			messages.success(request,"✔ Pomyślnie dodano nowe zgłoszenie.")
			return redirect('main')
	if request.method == "GET":
		form = TicketForm()
		return render(request, 'ticket_create.html', {'form': form})

@login_required
def ticket_list_view(request):
	if request.user.is_superuser:
		tickets = Ticket.objects.all()
	elif request.user.is_staff:
		tickets = Ticket.objects.filter(pracownik=request.user)
	else:
		tickets = Ticket.objects.filter(uzytkownik=request.user)

	ticket_filter = TicketFilter(request.GET, queryset=tickets)

	paginator = Paginator(ticket_filter.qs, 5)
	page_number = request.GET.get('page')
	tickets_page = paginator.get_page(page_number)

	context = {
		'filter': ticket_filter,
		'tickets': tickets_page,
		'paginator': paginator
	}

	return render(request, 'ticket_list.html', context)

@login_required
def ticket_detail_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    is_admin = request.user.is_superuser
    is_worker_of_this_ticket = request.user.is_staff and ticket.pracownik == request.user
    is_owner = ticket.uzytkownik == request.user

    if not (is_admin or is_worker_of_this_ticket or is_owner):
        return HttpResponseForbidden()

    is_worker_or_admin = is_admin or is_worker_of_this_ticket
    can_edit_description = is_admin or is_owner

    if request.method == 'POST':
        # Edycja opisu
        if can_edit_description and 'opis' in request.POST:
            new_opis = request.POST.get('opis')
            ticket.opis = new_opis
            ticket.save()
            messages.success(request, "📝 Opis został zaktualizowany.")
            return redirect('ticket_detail', ticket_id=ticket.id)

        # Zmiana statusu
        if is_worker_or_admin and 'nowy_status' in request.POST:
            new_status = request.POST.get('nowy_status')
            if new_status:
                ticket.status = new_status
                ticket.save()
                messages.success(request, "✔ Status został zaktualizowany.")
                return redirect('ticket_detail', ticket_id=ticket.id)

        # Dodawanie komentarza
        if is_worker_or_admin and 'uwagi' in request.POST:
            tresc = request.POST.get('uwagi')
            if tresc:
                Komentarz.objects.create(ticket=ticket, autor=request.user, tresc=tresc)
                messages.success(request, "💬 Komentarz dodany.")
                return redirect('ticket_detail', ticket_id=ticket.id)

    komentarze = ticket.komentarze.order_by('-data_dodania')

    context = {
        'ticket': ticket,
        'is_worker_or_admin': is_worker_or_admin,
        'can_edit_description': can_edit_description,
        'komentarze': komentarze
    }

    return render(request, 'ticket_detail.html', context)

@login_required
def usun_komentarz_view(request, komentarz_id):
    komentarz = get_object_or_404(Komentarz, id=komentarz_id)
    ticket = komentarz.ticket

    if request.user.is_superuser or (request.user == komentarz.autor):
        komentarz.delete()
        messages.success(request, "🗑 Komentarz został usunięty.")
        return redirect('ticket_detail', ticket_id=ticket.id)
    else:
        return HttpResponseForbidden("Nie masz uprawnień do usunięcia tego komentarza.")

def zmien_status_view(request, ticket_id):
	if request.method == "POST":
		ticket = get_object_or_404(Ticket, id=ticket_id)
		if request.user.is_superuser or (request.user.is_staff and ticket.pracownik == request.user):
			ticket.status = request.POST['nowy_status']
			ticket.save()
		else:
			return HttpResponseForbidden()
	return redirect('ticket_detail', ticket.id)

@login_required
def usun_ticket_view(request, ticket_id):
	ticket = get_object_or_404(Ticket, id=ticket_id)

	if request.user.is_superuser:
		ticket.delete()
		messages.success(request, "🗑 Zgłoszenie zostało usunięte.")
		return redirect('ticket-list')
	else:
		return HttpResponseForbidden("Nie masz uprawnień do usuwania zgłoszeń")

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def ticket_list_api(request):
	if request.method =='POST':
		serializer = TicketSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(uzytkownik=request.user)
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)

	if request.user.is_superuser:
		tickets = Ticket.objects.all()
	elif request.user.is_staff:
		tickets = Ticket.objects.filter(pracownik = request.user)
	else:
		tickets = Ticket.objects.filter(uzytkownik = request.user)

	status = request.GET.get('status')
	if status:
		tickets = tickets.filter(status=status)

	serializer = TicketSerializer(tickets, many=True)
	return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def ticket_update_api(request, ticket_id):
	ticket = get_object_or_404(Ticket, id=ticket_id)

	if ticket.uzytkownik != request.user and not request.user.is_superuser:
		return Response({"detail": "Brak dostępu"}, status=403)

	if ticket.status != 'nowe':
		return Response({"detail": "Nie można edytować zgłoszenia w tym statusie"}, status=400)

	serializer = TicketSerializer(ticket, data=request.data, partial=True)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	return Response(serializer.errors, status=400)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def zmien_status_api(request, ticket_id):
	ticket = get_object_or_404(Ticket, id=ticket_id)
	dozwolone_przejscia = {
		"nowe": "w trakcie",
		"w trakcie": "gotowe",
		"gotowe": "odebrane",
	}


	if not request.user.is_superuser and ticket.pracownik != request.user:
		return Response({"detail": "Brak dostępu do zmiany statusu"}, status=403)

	nowy_status = request.data.get("status")
	if nowy_status not in ['nowe', 'w trakcie', 'gotowe', 'odebrane']:
		return Response({"detail": "Niepoprawny status"}, status=400)

	if nowy_status != dozwolone_przejscia.get(ticket.status):
		return Response({"detail": "Nie można przeskoczyc statusów."}, status=400)
	ticket.status = nowy_status
	ticket.save()
	return Response({"status": ticket.status})

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def przypisanie_ticket_api(request, ticket_id):
	ticket = get_object_or_404(Ticket, id=ticket_id)

	if ticket.pracownik is not None:
		return Response({"detail": "Ticket już jest przypisany"}, status=400)
	if request.user.is_superuser or request.user.is_staff:
		ticket.pracownik = request.user
		ticket.save()
		serializer = TicketSerializer(ticket)
		return Response({"Dane": serializer.data}, status=200)

	return Response({"detail": "Brak uprawnień"}, status=403)




class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    serializer_class = GoogleSocialLoginSerializer






