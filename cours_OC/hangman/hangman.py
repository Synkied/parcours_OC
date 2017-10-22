from data import *
from functions import *

continue_game = True

print("-"*47)
print("Welcome to the Hangman Game! Get ready to play.")
print("-"*47)

scores = get_score()
user_name = get_user_name()



if user_name in scores.keys():
	print("Welcome back {}! Your score is: {}".format(user_name.capitalize(), scores[user_name]))

elif user_name not in scores.keys():
	scores[user_name] = 0

while continue_game != False:
	
	random_word = get_random_word()
	found_letters = []
	tried_letters = []
	word_to_guess = word_to_display(random_word, found_letters)
	
	num_chances = num_guesses


	while word_to_guess != random_word and num_chances > 0:
		print("Word to find:{}. Guesses left: {}".format(word_to_guess, num_chances))
		char_guess = get_letter_input()

		if char_guess in tried_letters:
			print("<"*30)
			print("You already tried that one.")
			print("<"*30)
		elif char_guess in found_letters:
			print(">"*30)
			print("You already got that one.")
			print(">"*30)
		elif char_guess in random_word:
			print("Good job, you got a letter!")
			found_letters.append(char_guess)
		else:
			print("This letter is not in the hidden word.")
			tried_letters.append(char_guess)
			num_chances-=1

		word_to_guess = word_to_display(random_word, found_letters)

		if word_to_guess == random_word:
			score = num_chances
			print("\n")
			print("*"*50)
			print("You win! The word was: {}. You got {} points.".format(random_word, score))
			print("*"*50)

			continue_game = play_again()

		elif num_chances == 0:
			print("\n")
			print("x"*80)
			print("You ran out of chances... You lose. HANGED! The word was: {}".format(random_word))
			print("x"*80)

			continue_game = play_again()

	scores[user_name] += num_chances

save_scores(scores)

print("Game finished, you now have {} points".format(scores[user_name]))