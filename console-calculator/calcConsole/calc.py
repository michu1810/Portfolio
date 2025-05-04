import math

historia = []

def liczby():

        dzialanie = input("\nJeśli chcesz zakończyć używanie kalkulatora napisz exit \n\n"
                          "Wybierz działanie spośrod podanych które chcesz wykonać:\nDodawanie (+),\nOdejmowanie (-),\nDzielenie (/),\nMnożenie (*),\nPotęgowanie (^),\nPierwiastek Drugiego Stopnia (pierwiastek2),\nPierwiastek Trzeciego Stopnia (pierwiastek3),\nModulo (%),\nLogarytm (log),\nSinus (sin),\nCosinus (cos),\nTangens (tan),\nSilnia (!)\n")
        if dzialanie.lower() == "exit":
            return "exit"

        if dzialanie in ["+", "-", "/", "*", "^", "%", "log"]:
            liczba1 = float(input("Podaj pierwszą liczbę: "))
            liczba2 = float(input("Podaj drugą Liczbę: "))
            return dzialanie, liczba1, liczba2
        elif dzialanie in ["!"]:
            liczba1 = int(input("Podaj liczbę dla której obliczyć silnię: "))
            return dzialanie, liczba1, None
        elif dzialanie in ["pierwiastek2", "pierwiastek3", "sin", "cos", "tan"]:
            liczba1 = float(input("Podaj pierwszą liczbę: "))
            return dzialanie, liczba1, None
        else:
            print("Niepoprawne działanie")
            return None




def kalkulator ():
    while True:
        wynik = None
        dane = liczby()
        if dane == "exit":
            with open("historia.txt", "r") as f:
                linie = f.readlines()
                start = len(linie)
            print("Czy chcesz zapisac historie dzialan do pliku?")
            f = input("(tak/nie)")
            if f == "tak":
                with open("historia.txt", "a") as f:
                    f.write(f"Zaktualizowano historie obliczen \n")
                    for i, wpis in enumerate(historia, start = start):
                        f.write(f"{i+1}. {wpis}\n")


            break

        if dane is None:
            continue

        dzialanie, liczba1, liczba2 = dane

        try:
            if dzialanie == "+":
                wynik = liczba1 + liczba2

            elif dzialanie == "-":
                wynik = liczba1 - liczba2
            elif dzialanie == "/":
                if liczba2 == 0:
                    print("Nie dzielimy przez 0!")
                    continue
                wynik = liczba1 / liczba2
            elif dzialanie == "*":
                wynik = liczba1 * liczba2
            elif dzialanie == "^":
                wynik = math.pow(liczba1, liczba2)
            elif dzialanie == "pierwiastek2":
                wynik = math.sqrt(liczba1)
            elif dzialanie == "pierwiastek3":
                wynik = math.cbrt(liczba1)
            elif dzialanie == "%":
                wynik = liczba1 % liczba2
            elif dzialanie == "log":
                wynik = math.log(liczba1, liczba2)
            elif dzialanie == "sin":
                wynik = round(math.sin(math.radians(liczba1)),2)
            elif dzialanie == "cos":
                wynik = round(math.cos(math.radians(liczba1)),2)
            elif dzialanie == "tan":
                wynik = round(math.tan(math.radians(liczba1)),2)
            elif dzialanie == "!":
                wynik = math.factorial(liczba1)
            else:
                print("Niepoprawne działanie spróbuj ponownie.")

            if wynik is not None:
                print("Wynik to: {:.2f}\n".format(wynik))
            if dzialanie in ["+", "-", "/", "*", "^", "%", "log"]:
                historia.append(f"{liczba1} {dzialanie} {liczba2} = {wynik}")
                print("Ostatnie działania to:", historia)
            elif dzialanie in ["pierwiastek2", "pierwiastek3", "sin", "cos", "tan", "!"]:
                historia.append(f"wynik {dzialanie} z liczby {liczba1} to {wynik}")
                print("Ostatnie działania to:", historia)
            else:
                print("Błąd!")


        except ValueError:

            print("Niepoprawna wartość! Podaj poprawne liczby.")
            continue


        except Exception as e:

            print("Wystąpił błąd:", e)
            continue


kalkulator()
