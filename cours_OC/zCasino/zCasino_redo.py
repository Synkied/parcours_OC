from random import randrange
from math import ceil


def betting(money):

	num_bet = -1
	bet = 0
	while num_bet < 0 or num_bet > 49:
		print("Please choose a number between 0 and 49:")
		try:
			num_bet = int(input())
		except ValueError:
			print("Please input a valid number:")
			continue
		if num_bet < 0:
			print("This is a negative number.")
		elif num_bet > 49:
			print("This number is superior to 49.")

	while bet <= 0:
		print("Place a bet")
		try:
			bet = int(input())
		except ValueError:
			print("This is not a number.")
		if bet > money:
			bet = money
	return num_bet, bet


def random_num(num_bet,bet,money):
	rand_num = randrange(50)
	print("The roulette turns and... {} is the number.".format(rand_num))
	if num_bet == rand_num:
		print("Nice one, you get", bet*3,"$.")
		money+=bet*3
		return money
	elif num_bet % 2 == rand_num % 2:
		print("Nice. You get {}$.".format(ceil(bet*(1/2))))
		money+=ceil(bet*(1/2))
		return money
	else:
		print("You lost {}$.".format(bet))
		money-=bet
		return money
	

def main():
	print("-"*56)
	print("="*15,"Welcome to the zCasino!!","="*15)
	print("-"*56)
	continuer = True
	money = 5000
	while continuer == True:
		

		num_bet, bet = betting(money)
		money = random_num(num_bet, bet, money)
		print("You have {}$.".format(money))
		print("\n")

		if money <= 0:
			print("Would you like to play again? (Y/N)")
			play = input().upper()

			if play == "Y":
				main()
				
			elif play =="N":
				continuer = False

	

if __name__ == "__main__":
	main()
	



