# Importujemy klasę Model i typy pól z Django – żeby móc tworzyć modele (czyli struktury do bazy danych)
from django.db import models

# Tworzymy model (czyli klasę, która będzie reprezentować jedno zadanie w bazie)
class Zadanie(models.Model):
    # Lista możliwych statusów dla zadania.
    # To jest lista krotek (tuple), gdzie pierwszy element to wartość w bazie,
    # a drugi to to, co będzie widoczne np. w panelu admina.
    TYTUL_STATUSU = [
        ('do zrobienia', 'Do zrobienia'),
        ('w trakcie', 'W trakcie'),
        ('zrobione', 'Zrobione'),
    ]

    # Pole tekstowe – tytuł zadania (maksymalna długość: 200 znaków)
    tytul = models.CharField(max_length=200)

    # Pole z ograniczonymi opcjami do wyboru – musimy podać choices
    # Użytkownik będzie wybierać jedną z trzech opcji podanych wyżej
    status = models.CharField(max_length=20, choices=TYTUL_STATUSU, default='do zrobienia')

    # Automatyczne ustawienie daty, kiedy zadanie zostało dodane
    data_dodania = models.DateTimeField(auto_now_add=True)

    # Specjalna metoda, która mówi Django, jak ten obiekt ma być wyświetlany jako tekst (np. w adminie)
    def __str__(self) -> str:
        # Zwracamy tytuł i status jako tekst
        return f"{self.tytul} ({self.status})"
    opis = models.TextField(blank=True)
