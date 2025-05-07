# 🛍️ Django Sklep Internetowy (PL)  
Ten projekt to aplikacja sklepu internetowego napisana w Django. Umożliwia przeglądanie produktów, filtrowanie po nazwie, marce, cenie i kategorii, dodawanie ich do koszyka, składanie zamówień oraz rejestrację i logowanie użytkowników. Projekt wykonałem korzystając głównie z dokumentacji i samodzielnych eksperymentów.

Celem projektu była nauka:
- obsługi widoków i sesji w Django,
- filtrowania danych z formularzy GET,
- paginacji i wiadomości (messages),
- stylowania aplikacji z użyciem własnego CSS.

---
### ✨ Główne funkcje aplikacji:

- 🔍 **Lista produktów z filtrowaniem** – filtruj po nazwie, marce, cenie oraz kategorii.
- 📦 **Koszyk** – dodawanie, usuwanie i aktualizacja produktów. Koszyk oparty na sesji.
- 🧾 **Checkout** – formularz zamówienia z danymi klienta i zapis do bazy danych.
- ✅ **Rejestracja / logowanie / wylogowanie** – wykorzystanie autoryzacji Django.
- 🛠️ **System powiadomień (messages)** – informacja o dodaniu do koszyka, złożeniu zamówienia i innych akcjach.
- 📄 **Paginacja** – lista produktów z podziałem na strony.
- 💡 **Responsywny frontend (HTML + CSS)** – prosta, przejrzysta szata graficzna.

### 🧠 Co się dzieje pod spodem (technicznie):

- Modele: `Product`, `Order`, `OrderItem`
- Widoki: CBV i FBV (`@require_POST`, `@login_required`)
- Sesja przechowuje koszyk
- `UserCreationForm` do rejestracji użytkowników
- `Paginator` do listy produktów
- `messages` do wyświetlania komunikatów
- Szablony HTML i własne style CSS

### 🔧 Technologie:
- Django 5.x
- SQLite3 (dev)
- HTML, CSS (własnoręcznie stylowane)
- Python 3.12

---

## 🇬🇧 About the project (EN)

Hi! 👋  
This is my first major Django project, built in 2 days after just about 3–4 weeks of learning Django. I learned everything from scratch by researching documentation, articles, and community posts. The goal was to build a fully working online shop – and I did it! 💪

### ✨ Key Features:

- 🔍 **Product listing with filters** – by name, brand, price, and category.
- 📦 **Shopping cart** – add, remove, and update items. Session-based.
- 🧾 **Checkout** – order form with user input, saved to the database.
- ✅ **User authentication** – register, log in, and log out using Django's auth system.
- 🛠️ **Message system** – feedback after actions (e.g., adding to cart, placing order).
- 📄 **Pagination** – paged product listing.
- 💡 **Responsive frontend (HTML + CSS)** – clean, minimal design.

### 🧠 Under the hood (tech stack):

- Models: `Product`, `Order`, `OrderItem`
- Views: CBV and FBV (`@require_POST`, `@login_required`)
- Cart stored in session
- `UserCreationForm` for registration
- `Paginator` for product pages
- `messages` for flash notifications
- Custom HTML templates and CSS styling

### 🛠 Technologies:
- Django 5.x
- SQLite3 (dev)
- HTML & custom CSS
- Python 3.12

---

## 💡 Co dalej?

Projekt można łatwo rozbudować o:
- panel admina dla zarządzania produktami,
- wysyłanie maili z potwierdzeniem zamówienia,
- integrację z płatnościami,
- API REST i frontend np. w React.

Dziękuję za uwagę! 🙌

---

