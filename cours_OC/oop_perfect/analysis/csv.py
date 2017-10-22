# encoding: utf-8

import os

import pprint
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class SetOfParliamentMember:

	def __init__(self, name):
		self.name = name

	def data_from_csv(self, csv_file):
		"""
		Creates a data frame from a specified csv file. Where each row is a row from the csv file
		"""
		self.dataframe = pd.read_csv(csv_file, sep=";") # reads the csv file with pandas to create a data frame

	def data_from_dataframe(self, dataframe):
		self.dataframe = dataframe

	def display_chart(self):
		"""
		Creates a chart to display from a data frame
		"""
		data = self.dataframe # takes the dataframe passed to the instance
		female_mps = data[data.sexe == "F"] # stores data that are equal to "F" for the col sexe
		male_mps = data[data.sexe == "H"]

		counts = [len(female_mps), len(male_mps)] # stores the number of elem in each sexe_mps
		counts = np.array(counts)
		nb_mps = sum(counts)
		proportions = counts / nb_mps

		labels = ["Female ({})".format(counts[0]), "Male ({})".format(counts[1])]

		fig, ax = plt.subplots()
		ax.axis("equal") # sets the window proportionally to avoid stretching of graphs
		ax.pie(proportions, labels=labels, autopct="%1.1f%%") # converts to percents the proportion, with a .1 precision

		plt.title("{} ({} Mps)".format(self.name, nb_mps)) # sets the title to the name of the instance + the number of mps
		plt.show()

	def split_by_political_party(self):
		result = {}
		data = self.dataframe # takes the dataframe passed to the instance

		all_parties = data["parti_ratt_financier"].dropna().unique() # dropna() drops N/A values. unique() keeps only one instance of values

		for party in all_parties:
			data_subset = data[data.parti_ratt_financier == party] # filters "data" var by party
			subset = SetOfParliamentMember("MPs from party {}".format(party)) # creates an instance of SetOfParliamentMember class, to filter by party
			subset.data_from_dataframe(data_subset) # 
			result[party] = subset # assigns "party" keys the "subset" values
		return result # returns the dict with "party" as keys and "subset as values

	def __str__(self):
		return str([mp.nom for row_index, mp in self.dataframe.iterrows()])

	def __repr__(self):
		return "SetOfParliamentMember: {} members".format(len(self.dataframe))

	def __len__(self):
		return self.number_of_mps

	def __contains__(self, mp_name):
		return mp_name in self.dataframe["nom"].values

	def __getitem__(self, index):
		try:
			result = dict(self.dataframe.iloc[index])
		except:
			if index < 0:
				raise Exception("Please select a positive index")
			elif index >= len(self.dataframe):
				raise Exception("There are only {} MPs!".format(len(self.dataframe)))
			else:
				raise Exception("Wrong index")
		return result

	def __add__(self, other):
		if not isinstance(other, SetOfParliamentMember):
			raise Exception("Can not add a SetOfParliamentMember with an object of type {}".format(type(other)))

		df1, df2 = self.dataframe, other.dataframe ##todo: ici il y a du packing/unpacking
		df = df1.append(df2)
		df = df.drop_duplicates()

		s = SetOfParliamentMember("{} - {}".format(self.name, other.name))
		s.data_from_dataframe(df)
		return s

	def __lt__(self, other):
		return self.number_of_mps < other.number_of_mps

	def __gt__(self, other):
		return self.number_of_mps > other.number_of_mps

	@property
	def number_of_mps(self):
		return len(self.dataframe)

	@number_of_mps.setter
	def number_of_mps(self, value):
		raise Exception("You can not set the number of MPs!")

	@classmethod
	def _register_parties(cl, parties):
		cl.ALL_REGISTERED_PARTIES = cl._group_two_lists_of_parties(cl.ALL_REGISTERED_PARTIES, list(parties))

	@classmethod
	def get_all_registered_parties(cl):
		return cl.ALL_REGISTERED_PARTIES

	@staticmethod
	def _group_two_lists_of_parties(original, new):
		return list(set(original + new)) # This line drop duplicates in the list 'original + new'



def launch_analysis(data_file,
					by_party = False, info = False, displaynames = False,
					searchname = None, index = None, groupfirst = None):

	sopm = SetOfParliamentMember("All MPs") # new instace with "All MPs" as name
	sopm.data_from_csv(os.path.join("data", data_file)) # analyze data from csv file specified by user, when he calls parite.py with args in a terminal
	sopm.display_chart()

	if by_party:
		for party, s in sopm.split_by_political_party().items():
			s.display_chart()

	if info:
		print()
		print(repr(sopm))

	if displaynames:
		print()
		print(sopm)

	if searchname != None:
		is_present = searchname in sopm
		print()
		print("Testing if {} is present: {}".format(searchname, is_present))

	if index is not None:
		index = int(index)
		print()
		pprint.pprint(sopm[index]) # prints the dict a nice way

	if groupfirst is not None:
		groupfirst = int(groupfirst)
		parties = sopm.split_by_political_party()
		parties = parties.values()
		parties_by_size = sorted(parties, reverse = True)

		print()
		print("Info: the {} biggest groups are :".format(groupfirst))
		for p in parties_by_size[0:groupfirst]:
			print(p.name)

		s = sum(parties_by_size[0:groupfirst])

		s.display_chart()

if __name__ == "__main__":
	launch_analysis('current_mps.csv')






def main():
	launch_analysis()



if __name__ == "__main__":
	main()