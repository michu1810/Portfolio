from random import randint

def main():
	x = randint(1, 10)
	tries = 0
	while tries < 5:
		user = int(input("Zgadnij liczbę z zakresu 1-10, masz tylko 5 prób!: "))
		if user > x:
			tries += 1
			print("Twoja liczba jest za duża, sprobuj ponownie.  Próba:", tries)
		elif user < x:
			tries +=1
			print("Twoja liczba jest za mała, sprobuj ponownie.  Próba:", tries)
		else:
			tries += 1
			print("Brawo zgadłeś wylosowaną liczbę! za",tries,"razem")
			play_again()



	if tries >= 5:
		print("Niestety nie udało ci się spróbuj ponownie")
		play_again()
def play_again():
	while True:
		play_again = input("Czy chcialbyś zagrać ponownie? (Tak lub Nie)")
		play_again = play_again.lower()
		if play_again == "tak":
			main()
		elif play_again == "nie":
			exit()
		else:
			print("Przepraszam ale podałeś błędna wartość")


main()
