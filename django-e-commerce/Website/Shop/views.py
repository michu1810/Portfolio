from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from decimal import Decimal, InvalidOperation
from .models import Product, Order, OrderItem
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator

def lista_produktow(request, page = 1):
	#FILTRY
	nazwa = request.GET.get('nazwa')
	marka = request.GET.get('marka')
	cena_min = request.GET.get('cena_min')
	cena_max = request.GET.get('cena_max')
	kategoria = request.GET.get('kategoria')

	produkty = Product.objects.all()

	if kategoria:
		produkty = produkty.filter(kategoria=kategoria)
	if nazwa:
		produkty = produkty.filter(nazwa__icontains=nazwa)
	if marka:
		produkty = produkty.filter(marka__icontains=marka)
	if cena_min:
		try:
				cena_decimal = Decimal(cena_min)
				produkty = produkty.filter(cena__gte=cena_decimal)
		except(InvalidOperation, ValueError):
			pass
	if cena_max:
		try:
				cena_decimal = Decimal(cena_max)
				produkty = produkty.filter(cena__lte=cena_decimal)
		except(InvalidOperation, ValueError):
			pass

	paginator = Paginator(produkty, 8)
	paginator_1 = request.GET.get('page', '1')

	page_obj = paginator.get_page(paginator_1)
	dostepne_kategorie = Product.CATEGORY_CHOICES



	return render(request, 'lista.html', {
		"page_obj" : page_obj,
		"paginator": paginator,
		"kategorie": dostepne_kategorie,
		"request": request

	})

@require_POST
def dodaj_do_koszyka(request, produkt_id):
	koszyk = request.session.get('koszyk', {})

	produkt_id = str(produkt_id)

	if produkt_id in koszyk:
		koszyk[produkt_id] += 1
	else:
		koszyk[produkt_id] = 1

	request.session['koszyk'] = koszyk
	messages.success(request, "Produkt został dodany do koszyka!")
	return redirect('lista_produktow')


def pokaz_koszyk(request):
	koszyk = request.session.get('koszyk', {})

	produkty = Product.objects.filter(id__in=koszyk.keys())
	suma = 0

	for produkt in produkty:
		ilosc = koszyk[str(produkt.id)]
		suma += produkt.cena * ilosc

	return render(request, 'koszyk.html', {
		"produkty" : produkty,
		'koszyk' : koszyk,
		'suma' : suma
	})

def usun_z_koszyka(request, produkt_id):
	koszyk = request.session.get('koszyk', {})

	produkt_id = str(produkt_id)

	if produkt_id in koszyk:
		del koszyk[produkt_id]

	request.session['koszyk'] = koszyk

	return redirect('pokaz_koszyk')

def aktualizuj_koszyk(request, produkt_id):
	koszyk = request.session.get('koszyk', {})

	produkt_id = str(produkt_id)
	try:
		ilosc = request.POST.get('ilosc')
		ilosc_int = int(ilosc)

		if ilosc_int <= 0:
			del koszyk[produkt_id]
		if ilosc_int > 0:
			koszyk[produkt_id] = ilosc_int
	except ValueError:
		pass
	request.session['koszyk'] = koszyk
	return redirect('pokaz_koszyk')


def szczegoly_produktu(request, produkt_id):
	produkt = get_object_or_404(Product, id=produkt_id)


	return render(request, 'szczegoly_produktu.html', {
		'produkt':produkt,
	})
def przekieruj_na_glowna():
	return redirect('lista_produktow')

@login_required()
def checkout_view(request):
	if request.method == "GET":
		koszyk = request.session.get('koszyk', {})
		produkty = Product.objects.filter(id__in=koszyk.keys())
		if not koszyk:
			return redirect('pokaz_koszyk')
		else:
			suma = 0
			for produkt in produkty:
				ilosc = koszyk[str(produkt.id)]
				suma += produkt.cena * ilosc
			return render(request, 'checkout.html', {
				"produkty": produkty,
				'koszyk': koszyk,
				'suma': suma
			})



	if request.method == "POST":
		imie = request.POST.get('imie')
		nazwisko = request.POST.get('nazwisko')
		adres = request.POST.get('adres')
		email = request.POST.get('email')
		nrtel = request.POST.get('nrtel')

		koszyk = request.session.get('koszyk', {})
		produkty = Product.objects.filter(id__in=koszyk.keys())


		suma = 0
		for produkt in produkty:
			ilosc = koszyk[str(produkt.id)]
			suma += produkt.cena * ilosc

		if koszyk:
			order = Order.objects.create(imie=imie, nazwisko=nazwisko, adres=adres, email=email, nrtel=nrtel, kwota=suma, data=datetime.now())
		for produkt in produkty:
			OrderItem.objects.create(zamowienie=order, produkt=produkt, ilosc=koszyk[str(produkt.id)], cena_jedn=produkt.cena)
		del request.session['koszyk']

		messages.success(request, "✔ Zamówienie zostało złożone!")

		return redirect('lista_produktow')

def register_view(request):
	if request.method =="POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "✔ Rejestracja zakończona! Możesz się teraz zalogować.")
			return redirect('login')
		return render(request, 'registration/register.html',{
			'form':form
		})

	if request.method == "GET":
		form = UserCreationForm()

		return render(request, 'registration/register.html', {
			'form': form
		})

def profile_view(request):

	return render(request, 'profile.html', {

	})

