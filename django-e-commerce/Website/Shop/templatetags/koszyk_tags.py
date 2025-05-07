from django import template

register = template.Library()

@register.filter
def dict_get(d, key):
    """
      Zwraca wartość ze słownika dla podanego klucza.
      Zapobiega błędom, jeśli klucz nie istnieje, zwracając None.
      """
    return d.get(str(key))  # konwertujemy klucz na string dla bezpieczeństwa
