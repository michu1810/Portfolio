from django.shortcuts import render, redirect, get_object_or_404
from .models import Ksiazka
from django.contrib import messages

def lista_ksiazek(request):


	status_filter = request.GET.get('status')
	title = request.GET.get('tytul')
	autor = request.GET.get('autor')
	sortowanie = request.GET.get('sortowanie')

	ksiazki = Ksiazka.objects.all()

	if sortowanie == 'tytul_asc':
		ksiazki = ksiazki.order_by('tytul')
	elif sortowanie == 'tytul_desc':
		ksiazki = ksiazki.order_by('-tytul')
	elif sortowanie == 'data_asc':
		ksiazki = ksiazki.order_by('data_dodania')
	elif sortowanie == 'data_desc':
		ksiazki = ksiazki.order_by('-data_dodania')


	if title:
		ksiazki = ksiazki.filter(tytul__icontains=title)

	if autor:
		ksiazki = ksiazki.filter(autor__icontains=autor)

	if status_filter and status_filter != 'wszystkie':
		ksiazki = ksiazki.filter(status=status_filter)


	return render(request, 'lista.html',{
		'ksiazki': ksiazki,
		'wybrany_status': status_filter


	})
def dodaj_ksiazke(request):
	if request.method == "POST":
		# Pobieramy dane z formularza z przegladarki
		tytul = request.POST.get('tytul')
		status = request.POST.get('status')
		autor = request.POST.get('autor')


		# Tworzymy nowe zadanie i zapisujemy do bazy danych
		Ksiazka.objects.create(tytul=tytul, status=status, autor=autor)
		messages.success(request, "✔ Książka została dodana!")

		# Po dodaniu przekierowujemy na listę zadań
		return redirect('lista_ksiazek')

	# Jesli uzytkownik dopiero wchodzi na strone (czyli metoda GET) - pokazujemy pusty formuklarz
	return render(request, 'dodaj.html')

def usun_ksiazke(request, id):
	ksiazka = get_object_or_404(Ksiazka, id=id)

	ksiazka.delete()
	messages.success(request, "🗑 Książka została usunięta!")

	return redirect('lista_ksiazek')

def edytuj_ksiazke(request,id):
	ksiazka = get_object_or_404(Ksiazka, id=id)

	if request.method == "POST":
		nowy_tytul = request.POST.get('tytul')
		nowy_autor = request.POST.get('autor')
		nowy_status = request.POST.get('status')

		ksiazka.tytul = nowy_tytul
		ksiazka.autor = nowy_autor
		ksiazka.status = nowy_status
		ksiazka.save()
		messages.success(request, "✏ Książka została zaktualizowana!")

		return redirect('lista_ksiazek')

	return render(request, 'edytuj.html', {'ksiazka': ksiazka})

def przekieruj_na_glowna(request):
	return redirect('lista_ksiazek')