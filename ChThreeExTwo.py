# Chapter Three Exercise Two - Create a variety of arrays

# Part A

import numpy as np
e= 2.718281828              # Defines e
array_a= np.ones(100)       # Creates an array of one hundred elements, each with a value of 1
array_a*= e                 # multiplies each of the elements in the array by e
print array_a               # Prints the array of one hundred elements, each with a value of e

# Part B

array_b= np.linspace(0, 360, 361) # Creates an array of all angles from 0 to 360, in 1-degree increments 
print array_b                     # Prints that array

# Part C

pi= 3.141592654            # Defines pi
array_c= array_b*(pi/180)  # Converts elements in array_b to radians, creating array_c
print array_c              # Prints array_c

# Part D

array_d= np.arange(12.0, 16.8, 0.2) # Creates an array, array_d, from 12 to 17, not including 17, with elements in increments of 0.2
print array_d                       # prints array_d

# Part E

array_e= np.arange(12.0, 17.2, 0.2)  #Creates an array, array_e, from 12 to 17, including 17, with elements in increments of 0.2
print array_e                        # Prints array_e
