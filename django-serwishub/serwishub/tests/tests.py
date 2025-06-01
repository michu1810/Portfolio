from django.test import TestCase
from django.urls import reverse

class MainViewTests(TestCase):
    """
    Testy widoku strony głównej (landing page).
    """

    def test_main_page_status_code(self):
        """
        Test sprawdza, czy strona główna zwraca status HTTP 200.
        """
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_main_page_template_used(self):
        """
        Test sprawdza, czy użyty jest właściwy szablon.
        """
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'main.html')
