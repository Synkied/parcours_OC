from random import shuffle, randrange
from constants import *

class MazeMaker:

	def __init__(self, lvl_file):
		self.lvl_file = lvl_file


	def make_maze(w = 15, h = 15):
		vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
		ver = [["| "] * w + ['|'] for _ in range(h)] + [[]]
		hor = [["+-"] * w + ['+'] for _ in range(h + 1)]

		def walk(x, y):
			vis[y][x] = 1

			d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
			shuffle(d)
			for (xx, yy) in d:
				if vis[yy][xx]: continue
				if xx == x: hor[max(y, yy)][x] = "+ "
				if yy == y: ver[y][max(x, xx)] = "  "
				walk(xx, yy)

		walk(randrange(w), randrange(h))

		s = ""
		for (a, b) in zip(hor, ver):
			s += ''.join(a + ['\n'] + b + ['\n'])
		return s

	with open(lvl_file, "w") as f:
		f.write(make_maze())