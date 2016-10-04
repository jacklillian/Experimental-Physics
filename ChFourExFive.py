# Chapter Four Exercise Five- reads in the given text file (created with TextWrangler) and reads it out in the given format

import numpy as np
f, a, da, = np.loadtxt("/Users/jacklillian/Desktop/ExerciseThreeData.txt", skiprows=4, unpack=True) # Reads in the textfile ExerciseThreeData.txt

np.savetxt('/Users/jacklillian/Desktop/ExerciseThreeDataOut.csv', zip( f, a, da), fmt="%0.16e",)   #Writes out a csv file version of the txt file from exercise three and four