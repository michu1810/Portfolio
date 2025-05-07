
# 🛍️ Django Sklep Internetowy – aplikacja sklepu online

Aplikacja webowa napisana w Django, która umożliwia przeglądanie, filtrowanie, dodawanie produktów do koszyka oraz składanie zamówień. Logika oparta jest na widokach funkcyjnych (FBV), z obsługą zapytań GET/POST, sesji oraz systemem wiadomości (messages) informujących o działaniach użytkownika.

Ten projekt stworzyłem w 2 dni po około 3–4 tygodniach nauki Django. Celem było zrozumienie podstaw logiki sklepu internetowego, obsługi koszyka, sesji i formularzy.

---

## 🔍 Funkcje

- ✅ Lista produktów z filtrowaniem po nazwie, marce, cenie i kategorii
- ✅ Paginacja listy produktów
- ✅ Szczegóły pojedynczego produktu z możliwością dodania do koszyka
- ✅ Koszyk działający na sesji: dodawanie, zmiana ilości, usuwanie
- ✅ Formularz zamówienia (checkout) – zapis do bazy danych
- ✅ Rejestracja i logowanie użytkownika (Django auth)
- ✅ Komunikaty po każdej akcji (messages)
- ✅ Prosty, przejrzysty interfejs (HTML + CSS)

---

## 🧠 Jak działa aplikacja

- Produkty pobierane są z bazy danych i filtrowane po `request.GET`.
- Paginacja (po 8 produktów) realizowana jest przez `Paginator`.
- Koszyk przechowywany jest w `request.session` jako słownik `{produkt_id: ilość}`.
- Formularz zamówienia zbiera dane użytkownika i tworzy wpisy w modelach `Order` i `OrderItem`.
- Komunikaty po dodaniu do koszyka lub złożeniu zamówienia wyświetlane są dzięki `messages.success(...)`.

---

## 🛠️ Technologie

- Python 3.12
- Django 5.x
- SQLite3 (dev)
- HTML + CSS (bez frameworków)
- System messages wbudowany w Django

---

## 🚀 Jak uruchomić lokalnie

```bash
git clone https://github.com/michu1810/django-sklep.git
cd django-sklep
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Aplikacja dostępna będzie pod `http://localhost:8000/Shop/lista/`

---

## 📁 Struktura projektu

```
django-sklep/
├── manage.py
├── Website/
│   ├── settings.py, urls.py
├── Shop/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   ├── templates/
│   ├── static/
│   └── migrations/
└── db.sqlite3
```

---

## ✍️ Autor

Michał Jamros  
[GitHub: michu1810](https://github.com/michu1810)

---

# 🛍️ Django Online Store – webshop project in Django

A web application built with Django that allows users to browse, filter and add products to a shopping cart, and place orders using a simple checkout form. The logic is based on function-based views (FBV), with GET/POST request handling, session-based cart management, and flash message notifications using Django's built-in `messages`.

This project was created in 2 days after around 3–4 weeks of learning Django. The goal was to practice core web development concepts: views, sessions, form handling, and database interaction.

---

## 🔍 Features

- ✅ Product list with filters: name, brand, price, category
- ✅ Pagination (8 products per page)
- ✅ Product detail page with "Add to cart" option
- ✅ Session-based shopping cart: add, remove, update quantity
- ✅ Order form (checkout) saving data to database
- ✅ User registration and login (Django auth system)
- ✅ Flash messages for key actions (cart, orders, etc.)
- ✅ Clean and minimal HTML + CSS interface

---

## 🧠 How it works

- Products are filtered using `request.GET` values.
- Pagination is handled with Django’s `Paginator`.
- Cart is stored in `request.session` as a Python dictionary `{product_id: quantity}`.
- Checkout form collects customer info and creates `Order` and `OrderItem` entries.
- `messages.success()` displays feedback for key user actions.

---

## 🛠️ Technologies

- Python 3.12
- Django 5.x
- SQLite3 (for development)
- HTML + custom CSS
- Django’s messages framework for alerts

---

## 🚀 How to run locally

```bash
git clone https://github.com/michu1810/django-sklep.git
cd django-sklep
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The app will be available at `http://localhost:8000/Shop/lista/`

---

## 📁 Project structure

```
django-sklep/
├── manage.py
├── Website/
│   ├── settings.py, urls.py
├── Shop/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   ├── templates/
│   ├── static/
│   └── migrations/
└── db.sqlite3
```

---

## ✍️ Author

Michał Jamros  
[GitHub: michu1810](https://github.com/michu1810)
