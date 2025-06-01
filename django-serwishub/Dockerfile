# Używamy oficjalnego obrazu Pythona 3.12
FROM python:3.12-slim

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy plik wymagań i instalujemy zależności
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy cały kod źródłowy
COPY . .

# Domyślny port uruchamiania serwera Django
EXPOSE 8000

# Komenda do uruchamiania serwera
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]