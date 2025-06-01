from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Hasło",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Powtórz hasło",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

        labels = {
            'email': 'Adres e-mail',
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
        }

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Hasła się nie zgadzają.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.rola = 'klient'
        if commit:
            user.save()
        return user

class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)


    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = authenticate(username=email, password=password)
        if not user:
            raise forms.ValidationError("Nieprawidłowy email lub hasło.")
        self.user = user
        return self.cleaned_data

    def get_user(self):
        return self.user