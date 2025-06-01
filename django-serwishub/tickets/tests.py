from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Ticket

User = get_user_model()

class TicketAPITestCase(APITestCase):
    """
    Testy API związane z obsługą zgłoszeń.
    """

    def setUp(self):
        # Tworzymy użytkownika testowego
        self.user = User.objects.create_user(email='testuser@example.com', password='pass123', rola='klient')
        self.client = APIClient()

        # Generujemy token JWT dla testowego użytkownika
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)

        # Ustawiamy nagłówek autoryzacji
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

        # Dodajemy przykładowe zgłoszenie
        self.ticket = Ticket.objects.create(tytul='Zgloszenie testowe', status='nowe', uzytkownik=self.user)

    def test_get_ticket_list(self):
        """
        Test pobierania listy zgłoszeń.
        """
        response = self.client.get('/api/tickets/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['tytul'], 'Zgloszenie testowe')

    def test_create_ticket(self):
        """
        Test tworzenia nowego zgłoszenia przez użytkownika.
        """
        data = {
            'tytul': 'Nowe zgłoszenie',
            'opis': 'Opis testowy'
        }
        response = self.client.post('/api/tickets/', data)
        # Oczekujemy statusu 201 Created
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Ticket.objects.filter(tytul='Nowe zgłoszenie').exists())

    def test_ticket_list_unauthorized(self):
        """
        Test próby pobrania listy zgłoszeń bez JWT.
        """
        self.client.credentials()  # Usuwamy token
        response = self.client.get('/api/tickets/')
        # Oczekujemy 401 Unauthorized
        self.assertEqual(response.status_code, 401)
