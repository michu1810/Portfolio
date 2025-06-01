from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site


User = get_user_model()

class UserTests(TestCase):
    """
    Testy związane z użytkownikami (rejestracja i logowanie).
    """

    def setUp(self):
        site = Site.objects.get_current()
        SocialApp.objects.create(
            provider='google',
            name='Google',
            client_id='test-id',
            secret='test-secret'
        ).sites.add(site)

    def test_user_registration(self):
        """
        Test sprawdza poprawną rejestrację użytkownika.
        """
        response = self.client.post(reverse('register'), {
            'email': 'test@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User',
            'rola': 'klient'
        })
        # Rejestracja powinna przekierować (302)
        self.assertEqual(response.status_code, 302)
        # Sprawdzamy, czy użytkownik został utworzony w bazie
        self.assertTrue(User.objects.filter(email='test@example.com').exists())

    def test_login_with_valid_credentials(self):
        """
        Test logowania użytkownika po rejestracji.
        """
        user = User.objects.create_user(email='user@example.com', password='testpass123')
        response = self.client.post(reverse('login'), {
            'email': 'user@example.com',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Powinno przekierować
        self.assertEqual(int(self.client.session['_auth_user_id']), user.pk)

    def test_login_with_invalid_credentials(self):
        """
        Test logowania z błędnymi danymi.
        """
        response = self.client.post(reverse('login'), {
            'email': 'nonexistent@example.com',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nieprawidłowy email lub hasło.")
