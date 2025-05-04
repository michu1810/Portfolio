from django.shortcuts import render, redirect, get_object_or_404
from .models import Wydatek
from django.contrib import messages
from django.db.models import Sum


def lista_wydatkow(request):

	kategoria = request.GET.get('kategoria')
	data_od = request.GET.get('data_od')
	data_do = request.GET.get('data_do')

	wydatki = Wydatek.objects.all()
	podsumowanie = (
		Wydatek.objects
		.values('data__year', 'data__month')
		.annotate(suma=Sum('kwota'))
	)
	print(podsumowanie)
	if kategoria and kategoria != 'wszystkie':
		wydatki = wydatki.filter(kategoria=kategoria)

	if data_od and data_do:
		wydatki = wydatki.filter(data__gte=data_od, data__lte=data_do)

	wydatki.values('data__year', 'data__month').annotate(suma=Sum('kwota'))





	return render(request, 'lista.html', {
		"wydatki": wydatki,
		"podsumowanie": podsumowanie,

	})

def dodaj_wydatek(request):
	if request.method == "POST":

		kwota = request.POST.get('kwota')
		opis = request.POST.get('opis')
		kategoria = request.POST.get('kategoria')
		data = request.POST.get('data')

		Wydatek.objects.create(kwota=kwota, opis=opis, kategoria=kategoria, data=data)
		messages.success(request, "✔ Wydatek został dodany!")


		return redirect('lista_wydatkow')

	# Jesli uzytkownik dopiero wchodzi na strone (czyli metoda GET) - pokazujemy pusty formuklarz
	return render(request, 'dodaj.html')

def edytuj_wydatek(request, id):
	wydatek = get_object_or_404(Wydatek, id=id)

	if request.method == "POST":
		nowy_opis = request.POST.get('opis')
		nowa_kwota = request.POST.get('kwota')
		nowa_kategoria = request.POST.get('kategoria')
		nowa_data = request.POST.get('data')

		wydatek.opis = nowy_opis
		wydatek.kwota = nowa_kwota
		wydatek.kategoria = nowa_kategoria
		wydatek.data = nowa_data
		wydatek.save()

		return redirect('lista_wydatkow')

	return render(request, 'edytuj.html', {'wydatek': wydatek})

def usun_wydatek(request, id):
	wydatek = get_object_or_404(Wydatek, id=id)

	wydatek.delete()
	return redirect('lista_wydatkow')
def przekieruj_na_glowna(request):
	return redirect('lista_wydatkow')




