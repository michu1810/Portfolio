### 📅 [Django To-Do App](./appDjango)

# 📅 Django To-Do App

Prosta aplikacja webowa napisana w Django, która pozwala tworzyć i zarządzać zadaniami. Projekt pozwala dodawać, edytować i usuwać zadania oraz przechowywać je w bazie SQLite. 

Cała logika aplikacji znajduje się w aplikacji `ideas`, w której definiuję modele (w tym przypadku model zadania), widoki obsługujące formularze oraz routing oparty o `urlpatterns`. Widoki są oparte na klasach generujących (Generic Class-Based Views), co pozwala mi na skrócenie kodu i lepsze rozdzielenie odpowiedzialności. Używam m.in. `ListView`, `CreateView`, `UpdateView` i `DeleteView`.

Do stylowania interfejsu wykorzystałem wbudowane szablony Django oraz prosty CSS, a dane są przechowywane lokalnie przy użyciu wbudowanej bazy SQLite. Formularze są zbudowane z `ModelForm`, co pozwala mi w łatwy sposób powiązać je bezpośrednio z bazą danych.

---

## 🔍 Funkcje

- ✅ Dodawanie nowych zadań (tytuł, opis)
- ✅ Edytowanie i usuwanie istniejących zadań
- ✅ Lista wszystkich zadań
- ✅ Prosty, przejrzysty interfejs
- ✅ Widoki CBV (Class-Based Views) do CRUD

---

## 🛠️ Technologie

- Python 3.11+
- Django 4.x
- SQLite3
- HTML + CSS (szablony Django)

---

## 🚀 Jak uruchomić lokalnie?

```bash
git clone https://github.com/michu1810/Portfolio.git
cd Portfolio/django-todo/appDjango
python manage.py runserver
```

Zainstaluj zależności:

```bash
pip install django
```

---

## 📁 Struktura projektu

```
appDjango/
├── manage.py
├── db.sqlite3
├── appDjango/
│   ├── settings.py, urls.py, wsgi.py, asgi.py
└── ideas/
    ├── models.py, views.py, urls.py
    ├── forms.py
    ├── templates/
    └── migrations/
```

---

## 🖊️ Autor

Michał Jamros  
[GitHub: michu1810](https://github.com/michu1810)

---

# 📅 Django To-Do App (EN)

A simple Django-based web application for managing personal tasks. Users can create, edit, and delete tasks. All data is stored in SQLite using Django ORM.

The entire logic is handled inside the `ideas` app, using Django's generic class-based views (`ListView`, `CreateView`, etc.), which allow clean and concise implementations of all CRUD operations. I used `ModelForm` to simplify form generation and validation tied directly to the model. The interface is rendered with Django templates and basic CSS styling.

---

## 🔍 Features

- ✅ Create new tasks (title, description)
- ✅ Edit or delete existing tasks
- ✅ Task listing view
- ✅ Simple, clean interface
- ✅ CBV (Class-Based Views) for CRUD

---

## 🛠️ Technologies

- Python 3.11+
- Django 4.x
- SQLite3
- HTML + CSS (Django templates)

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/michu1810/Portfolio.git
cd Portfolio/django-todo/appDjango
python manage.py runserver
```

Make sure Django is installed:

```bash
pip install django
```

---

## 📁 Project Structure

```
appDjango/
├── manage.py
├── db.sqlite3
├── appDjango/
│   ├── settings.py, urls.py, wsgi.py, asgi.py
└── ideas/
    ├── models.py, views.py, urls.py
    ├── forms.py
    ├── templates/
    └── migrations/
```

---

## 🖊️ Author

Michał Jamros  
[GitHub: michu1810](https://github.com/michu1810)
