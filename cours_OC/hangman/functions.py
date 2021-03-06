from data import *
from random import choice
import pickle
import os


def get_user_name():
	"""
	This function asks input from the user.
	The user enters a user_name. Must be between 4 and 16 chars, and only alphabetical [a_zA_Z].
	"""

	print("Please input your username:")
	user_name = input()

	if not user_name.isalpha() or len(user_name) < 4:
		print("Invalid username: {}. Between 4 and 16 chars and only in [a_zA_Z].".format(user_name)) 
		return get_user_name()
	else:
		return user_name

def get_score():

	"""
	This function seeks for an existing data_file with scores in it.
	If it does exist, loads the scores.
	Else, creates an empty dict.
	"""

	if os.path.exists(data_file_name):

		with open(data_file_name, 'rb') as data_file:
			saved_scores = pickle.Unpickler(data_file)
			scores = saved_scores.load()
	else:
		scores = {}

	return scores


def save_scores(scores):

	with open(data_file_name, 'wb') as data_file:
			saved_scores = pickle.Pickler(data_file)
			saved_scores.dump(scores)


def get_random_word():
	"""
	A function to get a random word from the word_list in "data.py"
	"""
	random_word = choice(word_list)
	return random_word


def get_letter_input():
	"""
	This function asks input from user.
	If the input is not a single alphabetical character, asks again.
	"""
	
	char_guess = input().lower()

	if len(char_guess) > 1 or not char_guess.isalpha():
		print("This is not a valid character. Please input one character at a time.")
		return get_letter_input()
	else:
		return char_guess

def word_to_display(random_word, found_letters):
	"""
	random_word is the word generated by get_random_word() (in this case scenario).
	found_letters is the list containing letters that the user inputs and that are in the random_word.
	For each char in random_word (in order), 
	If is in found_letters, append to hidden_word list.
	Else, append "_", to hide not found characters 
	"""

	hidden_word = []

	for char in random_word:
		if char in found_letters:
			hidden_word.append(char)
		else:
			hidden_word.append("_")

	return "".join(hidden_word)


def play_again():

	print("Would you like to play again? (Y/N)")
	play = input().upper()

	if play == "N":
		continue_game = False
	elif play == "Y":
		continue_game = True
	else:
		print("Please input Y or N.")
		return play_again()

	return continue_game