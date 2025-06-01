from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
	class Meta:
		model = Ticket
		fields = ['tytul', 'opis', 'status', 'zdjecie']
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['tytul'].widget.attrs['placeholder'] = 'Wpisz tytuł zgłoszenia'
		self.fields['status'].widget = forms.HiddenInput()
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

	def clean_tytul(self):
		tytul = self.cleaned_data['tytul']
		if len(tytul) < 5:
			raise forms.ValidationError("Tytuł musi mieć przynajmniej 5 znaków.")
		return tytul
