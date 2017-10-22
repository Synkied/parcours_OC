import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


decor_title = "#"*20
decor = "-"*20


print(decor_title, "\n", "Numpy".center(20), "\n", decor_title, sep="")
# numpy
panda_family = [[100, 5, 20, 80], [50, 2.5, 10, 40], [110, 6, 22, 80]]

panda_family_numpy = np.array(panda_family)

paws = panda_family_numpy[:, 0] #  for every list in the numpy array [:], get value at index 0

print(paws)
print(sum(paws))
print()


print(decor_title, "\n", "Pandas".center(20), "\n", decor_title, sep="")
# pandas
panda_family_df = pd.DataFrame(panda_family_numpy, index=["mom", "baby", "daddy"], columns=["paws", "hair", "tail", "belly"]) # Pandas knows how to work with numpy

print(panda_family_df)
print()
print(panda_family_df.belly) # prints the same thing as...
print()
print(panda_family_df["belly"]) # ... this.
print()
print(panda_family_df["belly"].values) # prints values in format numpy.ndarray
print(type(panda_family_df["belly"].values)) # check for the type
print()
print()


print(decor, "\n", "Using iterrows()".center(20), "\n", decor, sep="")
for line in panda_family_df.iterrows():
	index = line[0]
	content = line[1]
	print("Voici le panda: {}".format(index))
	print(content)
	print("-"*30)

print()
print(decor, "\n", "Using loc[] and iloc[]".center(20), "\n", decor, sep="")

print(panda_family_df.iloc[2]) # prints the elements at index location (iloc) of 2.
print()
print(panda_family_df.loc["daddy"]) # prints the elements at the specified label location (loc)

print()
print(decor, "\n", "Testing values".center(20), "\n", decor, sep="")
print(panda_family_df["belly"] == 80)
print()

mask = panda_family_df["belly"] == 80
pandas_80 = panda_family_df[mask]
pandas_not_80 = panda_family_df[~mask] # ~ reverses the mask

# More often written as :
# pandas_80 = panda_family_df[panda_family_df["belly"] == 80]
# or
# pandas_80 = panda_family_df[panda_family_df.belly == 80]

print(pandas_80)

print()
print(decor, "\n", "Modifying elements".center(20), "\n", decor, sep="")

new_pandas = pd.DataFrame(([[105,4,19,80],[100,5,20,80]]), index=["grandpa", "grandma"], columns=panda_family_df.columns)

all_pandas = panda_family_df.append(new_pandas)
print(all_pandas.drop_duplicates()) # grandma gets dropped as she is the same as mom

print()
panda_family_df["sexe"] = ["f","f","m"] # adding a new column, with values
print(panda_family_df)

print(len(panda_family_df)) # number of rows


print(decor_title, "\n", "MatPlotLib".center(20), "\n", decor_title, sep="")

ages = [25, 65, 26, 26, 46, 37, 36, 36, 28, 28, 57, 37, 48, 48, 37, 28, 60,
       25, 65, 46, 26, 46, 37, 36, 37, 29, 58, 47, 47, 48, 48, 47, 48, 60]


fig, ax = plt.subplots() # show one graph per window
# ax.hist(ages) # histogram
# plt.show()

plt.title("Women/Men comparison")
ax.pie([24, 18], labels=["Women", "Men"], autopct="%1.1f percents") # shows a circular diagram with 24 women and 18 men
ax.axis("equal") # makes axis equal, so there's no stretching of the diagram

plt.show()
