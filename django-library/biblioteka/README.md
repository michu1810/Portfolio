# 📚 Django Library App – aplikacja do zarządzania książkami

Aplikacja webowa stworzona w Django, która umożliwia dodawanie, filtrowanie, sortowanie i usuwanie książek w lokalnej bazie danych. Logika aplikacji oparta jest na klasycznych widokach funkcyjnych (FBV), z obsługą zapytań GET/POST i komunikatami Bootstrap.

Ten projekt został zbudowany jako ćwiczenie praktyczne do rozwijania pełnych umiejętności Django — obejmujących definiowanie modeli, logikę widoków, interakcję z użytkownikiem i przejrzyste renderowanie danych w szablonach.

W `views.py` obsługuję filtrowanie po tytule, autorze i statusie za pomocą parametrów GET. Sortowanie działa przez łańcuchy zapytań (`?sortowanie=...`). Tworzenie i usuwanie książek realizuję przez zapytania POST, a użytkownik otrzymuje informację zwrotną dzięki frameworkowi `messages` (np. "✔ Książka została dodana!"). Alerty Bootstrap są w pełni zamykalne bez przeładowania strony, co poprawia UX.

---

## 🔍 Funkcje

- ✅ Dodawanie książek (tytuł, autor, status)
- ✅ Usuwanie książek z potwierdzeniem
- ✅ Filtrowanie po statusie, tytule i autorze
- ✅ Sortowanie po tytule i dacie dodania (ASC/DESC)
- ✅ Komunikaty (Django messages + Bootstrap)
- ✅ Prosty i intuicyjny interfejs z Bootstrapem

---

## 🛠️ Technologie

- Python 3.11+
- Django 4.x
- SQLite3
- HTML + Bootstrap 5

---

## 🚀 Jak uruchomić lokalnie

```bash
git clone https://github.com/michu1810/Portfolio.git
cd Portfolio/django-library/biblioteka
python manage.py runserver
```

Upewnij się, że masz zainstalowanego Django:

```bash
pip install django
```

---

## 📁 Struktura projektu

```
biblioteka/
├── manage.py
├── db.sqlite3
├── biblioteka/
│   ├── settings.py, urls.py
└── ksiazki/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
    └── migrations/
```

---

## ✍️ Autor

Michał Jamros  
[GitHub: michu1810](https://github.com/michu1810)

---

# 📚 Django Library App (EN)

A Django-based web application for managing a personal library. Users can add, search, sort, and delete books. The logic is based on classic function-based views (FBV), with support for GET/POST handling and Bootstrap message alerts.

This project was built as a practical exercise to strengthen full-stack Django skills — covering model definition, view logic, user interaction, and clean rendering in templates.

In `views.py`, I handle filtering by title, author, and status using GET parameters. Sorting works via query strings (`?sortowanie=...`). Book creation and deletion is done via POST requests, and the user gets real-time feedback through the `messages` framework (e.g., "✔ Book added!"). Bootstrap alerts are fully dismissible without reloading the page, improving user experience.

---

## 🔍 Features

- ✅ Add books (title, author, status)
- ✅ Delete books with confirmation
- ✅ Filter by status, title, author
- ✅ Sort by title or date added (ASC/DESC)
- ✅ Message alerts (Django messages + Bootstrap)
- ✅ Simple and intuitive UI with Bootstrap

---

## 🛠️ Technologies

- Python 3.11+
- Django 4.x
- SQLite3
- HTML + Bootstrap 5

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/michu1810/Portfolio.git
cd Portfolio/django-library/biblioteka
python manage.py runserver
```

Make sure Django is installed:

```bash
pip install django
```

---

## 📁 Project Structure

```
biblioteka/
├── manage.py
├── db.sqlite3
├── biblioteka/
│   ├── settings.py, urls.py
└── ksiazki/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
    └── migrations/
```

---

## ✍️ Author

Michał Jamros  
[GitHub: michu1810](https://github.com/michu1810)
