from django.shortcuts import render, redirect, get_object_or_404
from .models import Zadanie # importujemy nasz model
from django.contrib import messages


# Tworzymy funkcje widoku ( czyli co ma sie dziac, gdy ktos wejdzie na strone / zadania / )
def lista_zadan(request):
	# Pobieramy z URL-a parametr "status", jeśli jest
	status_filter = request.GET.get('status')

	if status_filter:
		# Jeśli ktos kliknąl filtr - wybieramy tylko zadania o takim statusie
		zadania = Zadanie.objects.filter(status=status_filter)
	else:
		# Jeśli nie ma filtra - pokazujemy wszystkie
		zadania = Zadanie.objects.all()

	#Przekazujemy do szablonu listę zadań oraz wybrany filtr
	return render(request, 'lista.html', {
		'zadania': zadania,
		'wybrany_status': status_filter, # przyda sie do podswietlania aktywnego przycisku
		'ilosc_zadan': zadania.count()

	})

def dodaj_zadanie(request):
	if request.method == "POST":
		# Pobieramy dane z formularza z przegladarki
		tytul = request.POST.get('tytul')
		status = request.POST.get('status')
		opis = request.POST.get('opis')

		# Tworzymy nowe zadanie i zapisujemy do bazy danych
		Zadanie.objects.create(tytul = tytul, status= status, opis=opis)

		messages.success(request, "✔ Zadanie zostało dodane!")

		# Po dodaniu przekierowujemy na listę zadań
		return  redirect('lista_zadan')

# Jesli uzytkownik dopiero wchodzi na strone (czyli metoda GET) - pokazujemy pusty formuklarz
	return render(request, 'dodaj.html')
def usun_zadanie(request, id):
	# Szukamy zadania po ID, jesli nie istnieje - zwroci 404
	zadanie = get_object_or_404(Zadanie, id=id)

	# Usuwamy zadanie z bazy
	zadanie.delete()
	messages.success(request, "🗑 Zadanie zostało usunięte!")

	# Po usunieciu przekierowujemy z powrotem na listę
	return redirect('lista_zadan')
def edytuj_zadanie(request, id):
	# Szukamy zadania w bazie danych po ID - jak nie znajdzie, to 404
	zadanie = get_object_or_404(Zadanie, id=id)

	if request.method == "POST":
		# Pobieramy dane z formularza ( czyli nowe wartosci )
		nowy_tytul = request.POST.get('tytul')
		nowy_status = request.POST.get('status')
		nowy_opis = request.POST.get('opis')

		# Aktualizujemy obiekt zadania
		zadanie.tytul = nowy_tytul
		zadanie.status = nowy_status
		zadanie.opis = nowy_opis
		zadanie.save() # zapisujemy zmiany do bazy
		messages.success(request, "✏ Zadanie zostało zaktualizowane!")

		return redirect('lista_zadan')

	# Jeżeli to tylko wejscie na strone ( czyli GET ), to wyswietlamy formularz z danymi
	return render(request, 'edytuj.html', {'zadanie': zadanie})

def przelacz_status_checkboxa(request, id):
	# Sprawdzamy, czy to POST - czyli kliknieto checkbox
	if request.method == 'POST':
		zadanie = get_object_or_404(Zadanie, id=id)

		checkbox_wartosc = request.POST.get('checkbox_status')
		print("STATUS z formularza: ", checkbox_wartosc)

		# Jesli juz zrobione nie ruszamy
		if checkbox_wartosc == 'on':
			zadanie.status = 'zrobione'
		else:
			zadanie.status = 'do zrobienia'

		zadanie.save()
		messages.success(request, "✔ Zmieniono status zadania!")

	# Po kliknieciu wracamy na listę
	return redirect('lista_zadan')

def przekieruj_na_liste(request):
    return redirect('lista_zadan')