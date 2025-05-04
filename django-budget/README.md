### 💸 [Django Budget App](./Budzet)
# 💸 Budżet Domowy – Aplikacja Django

Aplikacja webowa stworzona w Django, służąca do zarządzania i śledzenia domowych wydatków. Umożliwia dodawanie, edytowanie oraz filtrowanie wydatków według daty i kategorii. Prosty i przejrzysty interfejs pozwala szybko kontrolować miesięczne podsumowania i historię transakcji.

---

## 🔍 Funkcje

✅ Dodawanie nowych wydatków (opis, kwota, kategoria, data)  
✅ Edytowanie i usuwanie istniejących transakcji  
✅ Filtrowanie po:
- dacie od / do  
- kategorii wydatków

✅ Miesięczne podsumowanie wydatków z dynamicznym zestawieniem  
✅ Intuicyjny i responsywny frontend oparty o HTML + CSS  
✅ Zabezpieczenie danych przez Django ORM (SQLite)

---

## 📷 Zrzuty ekranu

| Filtrowanie i podsumowanie | Lista wydatków |
|----------------------------|----------------|
| ![](../screens/screen1.png) | ![](../screens/screen2.png) |

---

## 🛠️ Technologie

- Python 3.11+
- Django 4.x
- SQLite 3
- HTML, CSS

---

## 🚀 Jak uruchomić lokalnie?

```bash
git clone https://github.com/michu1810/Portfolio.git
cd Portfolio/django-budget/Budzet
python manage.py runserver
```
Upewnij się, że masz wirtualne środowisko i zainstalowany Django:
pip install django

📁 Struktura
Budzet/
├── manage.py
├── db.sqlite3
├── Budzet/          ← konfiguracja Django (settings, urls)
└── wydatki/         ← główna aplikacja: modele, widoki, szablony

✍️ Autor
Michał Jamros
GitHub → michu1810

-------------------------------------------------------------------------------------------------------------------------------------------

#💸 Budget Tracker – Django Web App
A Django-based web application for managing and tracking personal expenses. Users can add, edit, and filter expenses by date and category. The clean and intuitive UI makes it easy to monitor monthly summaries and expense history.

--

## 🔍 Features

✅ Add new expenses (description, amount, category, date)
✅ Edit or delete existing transactions
✅ Filter by:
- date range
- expense category

✅ Monthly spending summary with live calculation
✅ Clean and responsive frontend (HTML + CSS)
✅ Data stored securely via Django ORM (SQLite)

--

## 📷 Screenshots

| Filter and Summary | Expense List |
|----------------------------|----------------|
| ![](../screens/screen1.png) | ![](../screens/screen2.png) |


--

## 🛠️ Technologies
Python 3.11+
Django 4.x
SQLite 3
HTML & CSS

--

## 🚀 How to Run Locally
```bash
git clone https://github.com/michu1810/Portfolio.git
cd Portfolio/django-budget/Budzet
python manage.py runserver
```

--

Make sure Django is installed:
pip install django

📁 Structure
Budzet/
├── manage.py
├── db.sqlite3
├── Budzet/          ← Django settings and config
└── wydatki/         ← main app: models, views, templates

✍️ Author
Michał Jamros
GitHub → michu1810


