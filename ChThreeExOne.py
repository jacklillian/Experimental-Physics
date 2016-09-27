# Chapter 3 Exercise 1 -  creates array, r, of 9 evenly spaced numbers from 0 to 29

import numpy as np

r= np.linspace(0, 29,9)

print r


r**=2                       # find the square of each element
print r

#Part i

r= np.linspace(0, 29, 9)
r+=r                        # Finds the value of 2r using addition
print r

r= np.linspace(0, 29, 9)
r*=2                       # Finds the value of 2r using multiplication
print r
