import pygame
from constants import *
from random import shuffle, randrange


# class MazeMaker:
# 	"""
# 	This creates a random maze
# 	"""

# 	def __init__(self, lvl_file):
# 		self.lvl_file = lvl_file

# 	def make_maze(w = 7, h = 7):
# 		vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
# 		ver = [["| "] * w + ['|'] for _ in range(h)] + [[]]
# 		hor = [["+-"] * w + ['+'] for _ in range(h + 1)]

# 		def walk(x, y):
# 			vis[y][x] = 1

# 			d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
# 			shuffle(d)
# 			for (xx, yy) in d:
# 				if vis[yy][xx]: continue
# 				if xx == x: hor[max(y, yy)][x] = "+ "
# 				if yy == y: ver[y][max(x, xx)] = "  "
# 				walk(xx, yy)

# 		walk(randrange(w), randrange(h))

# 		s = ""
# 		for (a, b) in zip(hor, ver):
# 			s += ''.join(a + ['\n'] + b + ['\n'])
# 		return s

# 	with open(lvl_file, "w") as f:
# 		f.write(make_maze())


class Level:
	"""
	This is to generate and display the level
	"""

	def __init__(self, lvl_file):
		self.lvl_file = lvl_file
		self.structure = 0


	def generate_lvl(self):
		# self.structure = MazeMaker(self.lvl_file)

		with open(self.lvl_file, "r") as lvl_file:
			structure_niveau = []
			#On parcourt les lignes du lvl_file
			for ligne in lvl_file:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le lvl_file
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau

	def display_lvl(self, window):
		wall = pygame.image.load(wall_img).convert()
		begin = pygame.image.load(begin_img).convert()
		arrival = pygame.image.load(arrival_img).convert_alpha()

		line_num = 0

		for line in self.structure:
			case_num = 0
			for sprite in line:
				x = case_num * sprite_size
				y = line_num * sprite_size
				
				

				if sprite == 'd':
					window.blit(begin, (x,y))

				if sprite == 'a':
					window.blit(arrival, (x,y))
				if sprite == 'm':
					window.blit(wall, (x,y))

				case_num += 1
			line_num += 1




class Char:

	def __init__(self, right, left, up, down, lvl):
		self.right = pygame.image.load(dk_right).convert_alpha()
		self.left = pygame.image.load(dk_left).convert_alpha()
		self.up = pygame.image.load(dk_up).convert_alpha()
		self.down = pygame.image.load(dk_down).convert_alpha()

		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0

		self.direction = self.right
		self.lvl = lvl


	def move(self, direction):

			if direction == "right":
				# to not get out of the screen
				if self.case_x < (nb_sprites - 1):
					# check if the case is not a wall
					if self.lvl.structure[self.case_y][self.case_x + 1] != "m":
						# if it is not, go by one case
						self.case_x += 1
						# move the dk_img on the case
						self.x = self.case_x * sprite_size
				# put the right image for the selected direction
				self.direction = self.right


			if direction == "left":
				if self.case_x > 0:
					if self.lvl.structure[self.case_y][self.case_x - 1] != "m":
						self.case_x -= 1
						self.x = self.case_x * sprite_size
				self.direction = self.left


			if direction == "up":
				if self.case_y > 0:
					if self.lvl.structure[self.case_y - 1][self.case_x] != "m":
						self.case_y -= 1
						self.y = self.case_y * sprite_size
				self.direction = self.up


			if direction == "down":
				if self.case_y < (nb_sprites -1) :
					if self.lvl.structure[self.case_y + 1][self.case_x] != "m":
						self.case_y += 1
						self.y = self.case_y * sprite_size
				self.direction = self.down



