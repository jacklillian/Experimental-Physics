# -*- coding: utf-8 -*-
# Chapter Four Exercise Four- reads in the given text file (created with TextWrangler) and reads it out in the given format

import numpy as np
f, a, da, = np.loadtxt("/Users/jacklillian/Desktop/ExerciseThreeData.txt", skiprows=4, unpack=True) # Reads in the textfile ExerciseThreeData.txt

info = 'Date: 2013–09–16'                                                                           # line 7-9 create the header for the txt file that is being written out
info+= '\nData taken by Liam and Selena'
info+= '\n\n    frequency (Hz)    amplitude (mm)    amp error (mm)    '

np.savetxt('/Users/jacklillian/Desktop/ExerciseThreeDataOut.txt', zip(f, a, da), fmt="%12.1f")      # Creates a new txt file with the header and arrays f, a, da


