from random import randrange
from math import ceil

def moneyLeft(money):
	if money >= 5000:
		print("="*10)
		print("I'm rich mofo! I got {money}$".format(money=money))
		print("="*10)
	if money < 5000 and money >= 2000:
		print("="*10)
		print("Not doing too bad. I got {money}$".format(money=money))
		print("="*10)
	if money < 2000:
		print("="*10)
		print("Fuck me. I got {money}$".format(money=money))
		print("="*10)


def betting(money):
	bet = 0
	bet_num = -1
	while bet_num < 0 or bet_num > 49:
		try:
			print("Please chose a number to bet on (between 0 and 49):")
			bet_num = int(input())
		except ValueError:
			bet_num = -1
			print("Please input a number between 0 and 49")

	while bet <= 0 or bet > money:
		try:
			print("Please state your bet: (if you bet more than you currently have, you bet everything you have.)")
			bet = int(input())
			if bet >= money:
				bet = money
		except ValueError:
			bet = 0
			print("Please input a number > 0")

	return bet_num, bet


def number_rand(money, bet_num, bet):

	random_num = randrange(50)
	print("\n")
	print("The roulette turns and it is... {random_num}!".format(random_num=random_num))

	if bet_num == random_num:
		money += (bet * 3)
		print("You get three times your bet!: ", bet*3)
		print("{}$ won, {}$ left".format(bet*3, money))
		print("-"*10)
		return money
	elif random_num % 2 == bet_num % 2:
		money += ceil(bet * (1/2))
		print("You get half your bet.")
		print("{ceil_bet}$ won, {money}$ left".format(ceil_bet=ceil(bet * (1/2)), money=money))
		print("-"*10)
		return money
	else:
		money -= bet
		print("You lost:", bet,"$")
		print("{money}$ left".format(money=money))
		print("-"*10)
		return money
		


def main():
	print("-"*56)
	print("="*15,"Welcome to the zCasino!!","="*15)
	print("-"*56)
	quitter = False
	money = 5000
	while not quitter:
		
		bet_num, bet = betting(money)
		money = number_rand(money, bet_num, bet)
		moneyLeft(money)

		if money == 0:
			print("You lost.")
			print("Do you want to play again ? Y/N")
			play = input().upper()
			if play == "Y":
				main()
			elif play == "N":
				quitter = True
			else:
				print("input Y or N please")


if __name__ == "__main__":
	main()