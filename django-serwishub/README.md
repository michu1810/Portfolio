# SerwisHub

**SerwisHub** to kompleksowa aplikacja webowa do zarządzania zgłoszeniami serwisowymi, stworzona w Django i Django REST Framework. Projekt stanowi pełne zaplecze backendowe – przygotowane REST API umożliwia łatwą integrację z dowolnym front-endem (webowym lub mobilnym). Nie zawiera front-endu – skoncentrowany jest na profesjonalnym zapleczu Django.

---

## 📚 Spis treści
- [📄 Opis projektu](#-opis-projektu)
- [🔧 Funkcjonalności](#-funkcjonalności)
- [💻 Technologie](#-technologie)
- [🚀 Instalacja i uruchomienie](#-instalacja-i-uruchomienie)
- [📦 API](#-api)
- [🔑 Role i uprawnienia](#-role-i-uprawnienia)
- [💡 Przykłady użycia](#-przykłady-użycia)
- [👤 Autor](#-autor)

---

## 📄 Opis projektu

SerwisHub umożliwia:
- tworzenie zgłoszeń serwisowych,
- przypisywanie ich do pracowników (wyłącznie w panelu admina Django),
- komentowanie zgłoszeń przez przypisanych pracowników i administratora,
- zarządzanie statusem w intuicyjnym workflow.

API jest w pełni gotowe do integracji z nowoczesnym front-endem (np. React, Vue, aplikacje mobilne).

---

## 🔧 Funkcjonalności

- **Tworzenie zgłoszeń**: tytuł, opis, zdjęcie (status początkowy: „nowe”).
- **Edycja opisu** zgłoszenia (bez zmiany tytułu).
- **Workflow statusów**: „nowe” → „w trakcie” → „gotowe” → „odebrane”.
- **Komentarze**: mogą dodawać tylko przypisani pracownicy oraz administrator.
- **Przypisywanie zgłoszeń**: wyłącznie przez admina w panelu Django.
- **Usuwanie zgłoszeń**: tylko superuser.
- **Panel admina** do pełnej kontroli.
- **Autoryzacja**: JWT (SimpleJWT) oraz Google OAuth2 (django-allauth).
- **Docker i docker-compose** – gotowe środowisko.

---

## 💻 Technologie

- **Backend**: Django 5, Django REST Framework
- **Baza danych**: SQLite3
- **Uwierzytelnianie**: JWT (SimpleJWT), Google OAuth2 (`django-allauth`)
- **API**: RESTful API, w pełni gotowe do integracji
- **Inne**:
  - `dj-rest-auth` – rejestracja, logowanie, odświeżanie tokenów
  - `django-filter` – filtrowanie zgłoszeń
  - `Pillow` – obsługa zdjęć

---

## 🚀 Instalacja i uruchomienie

### 1️⃣ Klonowanie repozytorium
```bash
git clone https://github.com/michu1810/Portfolio.git
cd Portfolio/django-serwishub
```

### 2️⃣ Uruchomienie w Docker
```bash
docker-compose up --build
```

### 3️⃣ Alternatywnie (lokalnie w Pythonie)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 4️⃣ Dostęp
- **Aplikacja:** http://localhost:8000  
- **Panel administratora:** http://localhost:8000/admin  
- **API:** http://localhost:8000/api/

---

## 📦 API

- **Autoryzacja JWT:**  
  ```
  POST /api/token/
  POST /api/token/refresh/
  ```

- **Logowanie przez Google:**  
  ```
  POST /dj-rest-auth/google/
  ```

- **Zarządzanie zgłoszeniami:**  
  - `POST /api/tickets/` – tworzenie zgłoszeń  
  - `GET /api/tickets/` – lista zgłoszeń (z filtrami, paginacją)  
  - `PATCH /api/tickets/<id>/zmien-status/` – zmiana statusu (wg workflow)  

- **Usuwanie zgłoszeń:**  
  - `POST /usun-ticket/<id>/` – tylko dla superuser  

- **Usuwanie komentarzy:**  
  - `POST /usun-komentarz/<id>/` – autor komentarza lub superuser  

Każdy endpoint jest chroniony przez `@IsAuthenticated` i wymaga poprawnego JWT.

---

## 🔑 Role i uprawnienia

- **Superuser:** pełny dostęp (w tym usuwanie zgłoszeń i komentarzy, przypisywanie pracowników w panelu admina).
- **Pracownik:** może komentować, usuwać komentarze dodane przez niego i zmieniać statusy przypisanych do niego zgłoszeń.
- **Zwykły użytkownik:** może tworzyć zgłoszenia i edytować ich opis.

---

## 💡 Przykłady użycia

### Tworzenie zgłoszenia
```bash
curl -X POST http://localhost:8000/api/tickets/ \
  -H "Authorization: Bearer <TWÓJ_TOKEN>" \
  -F "tytul=Problem z drukarką" \
  -F "opis=Nie działa drukarka" \
  -F "zdjecie=@drukarka.jpg"
```

### Zmiana statusu
```bash
curl -X PATCH http://localhost:8000/api/tickets/1/zmien-status/ \
  -H "Authorization: Bearer <TWÓJ_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"status": "w trakcie"}'
```

### Odświeżenie tokenu
```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "<TWÓJ_REFRESH_TOKEN>"}'
```

---

## 👤 Autor

Projekt stworzony przez Michała Jamros.  
Kontakt: jamros.michal2020@gmail.com

---

**Dziękuję za zainteresowanie projektem!**  
Chętnie odpowiem na pytania lub pomogę w dalszym rozwoju 🎉
