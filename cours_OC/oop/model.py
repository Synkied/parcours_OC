import json
import math

from collections import defaultdict # for income graph

import matplotlib as mil
mil.use("TkAgg")
import matplotlib.pyplot as plt

class Agent:
	def __init__(self, position, **agent_attributes): # initialize the Agent class with **kwargs (a dictionary with unknown number of k:v pairs); packing keyword args in a dict {}
		self.position = position
		for attr_name, attr_value in agent_attributes.items(): # (items() returns a list of tuple pairs, on which it's possible to iterate)
			setattr(self, attr_name, attr_value) # sets all the key:value pairs to instances of the class Agent
			

class Position:
	def __init__(self, longitude_degrees, latitude_degrees):
		# We store the degree values, but we will be mostly using radians
        # because they are much more convenient for computation purposes.

        # assert : Lève une exception si renvoie False
		assert -180 <= longitude_degrees <= 180
		self.longitude_degrees = longitude_degrees

		assert -90 <= latitude_degrees <= 90
		self.latitude_degrees = latitude_degrees

	@property
	def longitude(self):
		# Longitude in radians
		return self.longitude_degrees * math.pi / 180

	@property
	def latitude(self):
		# Latitude in radians
		return self.latitude_degrees * math.pi / 180

	def __str__(self):

		return "{}, {}".format(self.longitude_degrees, self.latitude_degrees)


class Zone:
	"""
	A rectangular geographic area bounded by two corners. The corners can
	be top-left and bottom right, or top-right and bottom-left so you should be
	careful when computing the distances between them.
	"""
	ZONES = []
	EARTH_RADIUS_KILOMETERS = 6371
	MIN_LONGITUDE_DEGREES = -180
	MAX_LONGITUDE_DEGREES = 180
	MIN_LATITUDE_DEGREES = -90
	MAX_LATITUDE_DEGREES = 90
	WIDTH_DEGREES = 1 # degrees of longitude
	HEIGHT_DEGREES = 1 # degrees of latitude

	def __init__(self, corner1, corner2):
		self.corner1 = corner1
		self.corner2 = corner2
		self.inhabitants_list = []

	@property
	def width(self):
		return abs(self.corner1.longitude - self.corner2.longitude) * self.EARTH_RADIUS_KILOMETERS

	@property
	def height(self):
		return abs(self.corner1.latitude - self.corner2.latitude) * self.EARTH_RADIUS_KILOMETERS

	@property
	def area(self):
		return self.height * self.width

	def population_density(self):
		"""Population density of the zone, (people/km²)"""
		# Note that this will crash with a ZeroDivisionError if the zone has 0
		# area, but it should really not happen
		return self.population / self.area

	def average_agreeableness(self):
		if not self.inhabitants_list:
			return 0
		return sum([inhabitant.agreeableness for inhabitant in self.inhabitants_list]) / self.population

	@property
	def population(self):
		return len(self.inhabitants_list)

	def add_inhabitant(self, inhabitant):
		self.inhabitants_list.append(inhabitant)

	def contains(self, position):
		return position.longitude >= min(self.corner1.longitude, self.corner2.longitude) and \
			position.longitude < max(self.corner1.longitude, self.corner2.longitude) and \
			position.latitude >= min(self.corner1.latitude, self.corner2.latitude) and \
			position.latitude < max(self.corner1.latitude, self.corner2.latitude)

	@classmethod
	def _initialize_zones(cls):
		for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES): # range(-90, 90, 1)
			for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES): # range(-180, 180, 1)
				bottom_left_corner = Position(longitude, latitude)
				top_right_corner = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
				zone = Zone(bottom_left_corner, top_right_corner)
				cls.ZONES.append(zone)

	@classmethod
	def find_zone_that_contains(cls, position):
		if not cls.ZONES:
			cls._initialize_zones()
		# Compute the index in the ZONES array that contains the given position. i.e.: 44560 is the index of first agent's position in the file agents-100k.json
		# Verify it with the calcul below. 
		# longitudex_index = 100+180/1 = 280.
		# latitude_index = 33+90/1 = 123
		# longitude_bins = 360
		# zone_index = (123*360)+280 = 44560
		longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES)/ cls.WIDTH_DEGREES)
		latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES)/ cls.HEIGHT_DEGREES)
		longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES) # 180-(-180) / 1
		zone_index = latitude_index * longitude_bins + longitude_index

		# Just checking that the index is correct
		zone = cls.ZONES[zone_index]
		assert zone.contains(position)

		return zone


class BaseGraph:
	def __init__(self):
		self.title = "graph title"
		self.x_label = "x axis label"
		self.y_label = "y axis label"
		self.show_grid = True

	def show(self, zones):
		x_values, y_values = self.xy_values(zones)
		plt.plot(x_values, y_values, ".")
		plt.xlabel(self.x_label)
		plt.ylabel(self.y_label)
		plt.title(self.title)
		plt.grid(self.show_grid)
		plt.show()

	def xy_values(self, zones):
		raise NotImplementedError

class AgreeablenessGraph(BaseGraph):

	def __init__(self):
		super().__init__()
		self.title = "Nice people live in the countryside"
		self.x_label = "x - population density"
		self.y_label = "y - agreeableness"

	def xy_values(self, zones):
		x_values = [zone.population_density() for zone in zones]
		y_values = [zone.average_agreeableness() for zone in zones]
		return x_values, y_values

class IncomeGraph(BaseGraph):
	# Inheritance, yay!

	def __init__(self):
		# Call base constructor
		super(IncomeGraph, self).__init__()

		self.title = "Older people have more money"
		self.x_label = "age"
		self.y_label = "income"

	def xy_values(self, zones):
		income_by_age = defaultdict(float)
		population_by_age = defaultdict(int)
		for zone in zones:
			for inhabitant in zone.inhabitants_list:
				income_by_age[inhabitant.age] += inhabitant.income
				population_by_age[inhabitant.age] += 1

		x_values = range(0, 100)
		y_values = [income_by_age[age] / (population_by_age[age] or 1) for age in range(0, 100)]
		return x_values, y_values




def main():
	for agent_attributes in json.load(open("agents-100k.json")): # loads the agents in the json file into a python dictionary
		"""
		We pop latitude and longitude first, to avoid having duplicates when we unpack **agent_attributes in our instatiation
		"""
		latitude = agent_attributes.pop("latitude") # returns and pops the value of the latitudes keys in the agent_attributes dictionary 
		longitude = agent_attributes.pop("longitude")

		position = Position(longitude, latitude) # instantiate an object "position" with latitude and longitude as attributes

		agent = Agent(position, **agent_attributes) # instantiate an object "agent" with **kwargs attributes (named attributes, dictionary); unpacking (k=v, k=v, k=v, ...)
		zone = Zone.find_zone_that_contains(position)
		zone.add_inhabitant(agent)
		# print("Zone pop.:{}".format(zone.population))
		# print(zone.corner1, zone.corner2)
	agreeableness_graph = AgreeablenessGraph()
	agreeableness_graph.show(Zone.ZONES)

	income_graph = IncomeGraph()
	income_graph.show(Zone.ZONES)


if __name__ == main(): # if the python script is executed from this file...
	main() # ... execute the "main" function