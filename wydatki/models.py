from django.db import models

class Wydatek(models.Model):
	KATEGORIE = [
		("zywnosc", "Żywność"),
		("samochod", "Samochód"),
		("mieszkanie", "Mieszkanie"),
		("wlasne potrzeby", "Własne potrzeby"),
		("kredyt", "Kredyt"),
		("ogolna", "Ogólna"),
		("nagle wydatki", "Nagłe wydatki")
	]



	kwota = models.DecimalField(max_digits=10, decimal_places=2)
	opis = models.TextField()
	kategoria = models.CharField(max_length=250, choices=KATEGORIE, default="ogólna")
	data = models.DateField()
