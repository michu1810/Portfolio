from django.db import models
from django.conf import settings

class Ticket(models.Model):
	STATUS_CHOICES = [
		('nowe', 'Nowe'),
		('gotowe', 'Gotowe'),
		('w trakcie', 'W trakcie'),
		('odebrane', 'Odebrane'),
	]

	tytul = models.CharField(max_length=100)
	opis = models.TextField(blank=True)
	data_utworzenia = models.DateTimeField(auto_now_add=True)
	status = models.CharField(choices=STATUS_CHOICES, max_length=100, default='nowe')
	zdjecie = models.ImageField(upload_to='ticket_zdjecia/', blank=True, null=True)
	uzytkownik = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=None)
	pracownik = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=None, on_delete=models.SET_NULL, related_name="tickety_przypisane")

	def __str__(self) -> str:
		return f"{self.tytul} {self.opis} {self.status}"

class Komentarz(models.Model):
	ticket = models.ForeignKey('Ticket', related_name='komentarze', on_delete=models.CASCADE)
	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	tresc = models.TextField()
	data_dodania = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.autor} - {self.data_dodania.strftime('%d.%m.%Y %H:%M')}"