from django.db import models

class Product(models.Model):
	CATEGORY_CHOICES = [
		('obuwie', 'Obuwie'),
		('nakrycia glowy', 'Nakrycia głowy'),
		('bielizna', 'Bielizna'),
		('skarpety', 'Skarpety'),
		('bluzy', 'Bluzy'),
		('swetry i kardigany', 'Swetry i kardigany'),
		('koszulki', 'Koszulki'),
		('koszule', 'Koszule'),
		('spodnie', 'Spodnie'),
		('jeansy', 'Jeansy'),
		('spodenki', 'Spodenki'),
		('plaszcze', 'Płaszcze'),
		('kurtki', 'Kurtki'),
		('garnitury i akcesoria', 'Garnitury i akcesoria'),
	]


	nazwa = models.CharField(max_length=100)
	marka = models.CharField(max_length=100, default="Brak")
	cena = models.DecimalField(max_digits=10, decimal_places=2)
	opis = models.TextField(blank=True)
	kategoria = models.CharField(choices=CATEGORY_CHOICES, max_length=100, default='zobacz wszystko')
	zdjecie = models.ImageField(upload_to='')


	def __str__(self) -> str:
		return f"{self.nazwa} {self.marka} {self.opis} ({self.kategoria})"

class Order(models.Model):

	data = models.DateTimeField()
	kwota = models.DecimalField(max_digits=10, decimal_places=2)
	imie = models.CharField(max_length=50)
	nazwisko = models.CharField(max_length=50)
	adres = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	nrtel = models.CharField(max_length=12)

class OrderItem(models.Model):
	produkt = models.ForeignKey(Product, on_delete=models.CASCADE)
	zamowienie = models.ForeignKey(Order, on_delete=models.CASCADE)
	ilosc = models.IntegerField()
	cena_jedn = models.DecimalField(max_digits=10, decimal_places=2)
