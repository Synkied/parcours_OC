# encoding: utf-8

import os
import logging as lg




def launch_analysis(data_file):

	directory = os.path.dirname(os.path.dirname(__file__)) # getting the path to the current file
	path_to_file = os.path.join(directory, "data", data_file) # with this path, we go inside the parent folder and the folder `data` to get the file.


	try:
		with open(path_to_file, "r") as f:
			preview = f.readline()
		lg.info("Yeah, we managed to read the file. Here is a preview:{} ".format(preview))

	except FileNotFoundError as fnferr:
		lg.critical("Oh, file not found. Original message of the error: {}".format(fnferr))

	except:
		lg.error("Destination unknown")






def main():
	launch_analysis()



if __name__ == "__main__":
	main()