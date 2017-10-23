"""
Game: Donkey Kong Maze
Creator: Quentin Lathiere

The game is all about Donkey Kong going through a maze to get bananas.

Python scripts used:
dkmaze.py
constants.py
classes.py
"""
from constants import *
from classes import *
from pygame.locals import *
import pygame

pygame.init()

# window and images settings
window = pygame.display.set_mode((window_side, window_side)) # set window size

# icon settings
icon = pygame.image.load(icon_img).convert_alpha()
pygame.display.set_icon(icon)

# window title setting
pygame.display.set_caption(window_title)


continue_game = True

while continue_game:

	menu_bckgrd = pygame.image.load(menu_img).convert()
	window.blit(menu_bckgrd, (0,0))

	pygame.display.flip()

	in_menu = True
	in_game = True

	while in_menu:
		pygame.time.Clock().tick(30)
		pygame.display.set_caption(window_title_menu)

		for event in pygame.event.get():

			# quitting the game
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continue_game = False
				in_menu = False
				in_game = False

				choix = 0

			elif event.type == KEYDOWN:
				if event.key == K_F1:
					in_menu = False
					choix = "n1.txt"

			elif event.type == KEYDOWN:
				if event.key == K_F2:
					in_menu = False
					choix = "n2.txt"

	if choix != 0:

		game_bckgrd = pygame.image.load(game_img).convert()

		lvl = Level(choix)
		lvl.generate_lvl()
		lvl.display_lvl(window)

		dk = Char(dk_right, dk_left, dk_up, dk_down, lvl)



	while in_game:
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			# quitting the game
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continue_game = False
				in_menu = False
				in_game = False

			if event.type == KEYDOWN:
				if event.key == K_RIGHT:
					dk.move("right")
				if event.key == K_LEFT:
					dk.move("left")
				if event.key == K_UP:
					dk.move("up")
				if event.key == K_DOWN:
					dk.move("down")
				

		
		window.blit(game_bckgrd, (0,0))
		
		lvl.display_lvl(window)
		window.blit(dk.direction, (dk.x, dk.y))

		pygame.display.flip()


		if lvl.structure[dk.case_x][dk.case_y] == "a":
			print("WIN")
			in_game = False






