import django_filters
from .models import Ticket
from django import forms

class TicketFilter(django_filters.FilterSet):
	date = django_filters.DateFilter(
		field_name='data_utworzenia__date',
		label='Data',
		lookup_expr='exact',
		widget=forms.DateInput(attrs={
			'type': 'date',
			'class': 'form-control d-inline w-auto'
		})
	)
	status = django_filters.ChoiceFilter(
		choices=Ticket.STATUS_CHOICES,
		label='Status',
		widget=forms.Select(attrs={
			'class': 'form-select d-inline w-auto'
		})
	)

	class Meta:
		model = Ticket
		fields =['status', 'date']