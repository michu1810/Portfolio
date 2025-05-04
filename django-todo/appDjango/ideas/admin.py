from django.contrib import admin
from .models import Zadanie


@admin.register(Zadanie)

class ZadanieAdmin(admin.ModelAdmin):
	list_display = ('id', 'tytul', 'status', 'data_dodania')
	list_filter = ('status',)
	search_fields = ('tytul',)