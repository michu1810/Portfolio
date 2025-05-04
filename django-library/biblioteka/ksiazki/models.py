from random import choices
from django.db import models


class Ksiazka(models.Model):
	STATUSY = [
		('do przeczytania', 'Do przeczytania'),
		('czytam', 'Czytam'),
		('przeczytana', 'Przeczytana'),
	]

	tytul = models.CharField(max_length=200)
	autor = models.CharField(max_length=100)
	status = models.CharField(max_length=20, choices=STATUSY, default='do przeczytania')
	data_dodania = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.tytul} - {self.autor} ({self.status})"
