# 🧮 Python Calculator – konsolowy kalkulator naukowy

Ten projekt to prosty, ale rozbudowany kalkulator konsolowy napisany w Pythonie. Obsługuje zarówno podstawowe działania matematyczne, jak i funkcje trygonometryczne, logarytmy czy potęgowanie. Celem projektu była nauka przetwarzania danych wejściowych, pracy z wyjątkami (`try/except`) oraz logiki warunkowej w Pythonie.

Wszystkie działania zapisują się w liście `historia`, a na zakończenie można zapisać historię do pliku `historia.txt`. Zastosowałem pętlę `while`, funkcje, obsługę błędów, import `math`, zaokrąglanie wyników trygonometrycznych oraz sprawdzenie dzielenia przez zero.

---

## 🔍 Funkcje

- ✅ Dodawanie, odejmowanie, mnożenie, dzielenie
- ✅ Potęgowanie i pierwiastkowanie (stopień 2 i 3)
- ✅ Działania trygonometryczne (sin, cos, tan – z konwersją stopni)
- ✅ Modulo (%) i logarytm o dowolnej podstawie
- ✅ Silnia (!)
- ✅ Obsługa błędów: dzielenie przez 0, błędny typ wejścia
- ✅ Historia działań wyświetlana po każdym działaniu i zapisywana do pliku

---

## 🧠 Użyte mechanizmy

- `math.pow`, `math.sqrt`, `math.cbrt`, `math.sin/cos/tan`, `math.factorial`, `math.log`
- `round(..., 2)` dla dokładnych wyników trygonometrycznych
- `try/except` dla obsługi błędów użytkownika i wyjątków
- `input()` + `float()`/`int()` do pobierania danych
- `historia.append(...)` do śledzenia przebiegu

---

## 🚀 Jak uruchomić?

1. Upewnij się, że masz zainstalowanego Pythona (3.11+):

```bash
python calc.py
```

2. Program działa w konsoli – wpisujesz działanie, np. `+`, `sin`, `log`, itd.

3. Aby zakończyć, wpisz `exit`. Program zapyta, czy zapisać historię do pliku.

---

## 📄 Przykładowa historia (`historia.txt`)

```
Zaktualizowano historie obliczen 
1. 2.0 + 2.0 = 4.0
Zaktualizowano historie obliczen 
3. 12.0 log 3.0 = 2.2618595071429146
```

---

## ✍️ Autor

Michał Jamros  
[GitHub: michu1810](https://github.com/michu1810)

---

# 🧮 Python Calculator – Console-Based Scientific Calculator

This project is a simple yet advanced console calculator written in Python. It supports both basic mathematical operations and more advanced functions such as trigonometry, logarithms, and exponentiation. The goal of the project was to practice handling user input, `try/except` exception handling, and conditional logic in Python.

All operations are stored in a list called `historia`, and at the end of the session the user is prompted to save the history into a `historia.txt` file. The project makes use of a `while` loop, functions, error handling, the `math` module, rounding of trigonometric results, and protection against division by zero.

---

## 🔍 Features

- ✅ Addition, subtraction, multiplication, division  
- ✅ Exponentiation and root calculation (square and cube root)  
- ✅ Trigonometric functions (sin, cos, tan – with degree conversion)  
- ✅ Modulo (%) and logarithms with custom base  
- ✅ Factorial (!)  
- ✅ Error handling: division by 0, invalid input types  
- ✅ Action history displayed after each operation and optionally saved to a file

---

## 🧠 Technical Overview

- `math.pow`, `math.sqrt`, `math.cbrt`, `math.sin/cos/tan`, `math.factorial`, `math.log`  
- `round(..., 2)` for clean trigonometric results  
- `try/except` blocks to handle user input and unexpected exceptions  
- `input()` + `float()`/`int()` for dynamic data input  
- `historia.append(...)` used to track calculation history  

---

## 🚀 How to Run

1. Make sure Python (3.11+) is installed:

```bash
python calc.py
```

## 📄 Example History (historia.txt)

```
Zaktualizowano historie obliczen 
1. 2.0 + 2.0 = 4.0
Zaktualizowano historie obliczen 
3. 12.0 log 3.0 = 2.2618595071429146
```

---

## ✍️ Author

Michał Jamros  
[GitHub: michu1810](https://github.com/michu1810)

