# Chapter Four Exercise Three- reads in the given text file (created with TextWrangler) and reads it out in the given format

import numpy as np
f, a, da, = np.loadtxt("/Users/jacklillian/Desktop/ExerciseThreeData.txt", skiprows=4, unpack=True) # Reads in the textfile ExerciseThreeData.txt
print f                                                                                             # Prints f, a, and da, the values of the columns in the data file
print a 
print da 