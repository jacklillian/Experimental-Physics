# Chapter Four Exercise Two - uses the zip function to creat an object out of three arrays, a, b, and c. Then turns that object back into a numpy array using numpy.asarray function

import numpy as np

a= np.array([1, 3, 5, 7])
b= np.array([8, 7, 5, 4])
c= np.array([0, 9,-6,-8])

d= zip(a,b,c)     # d is a list of tuples where the "i"th tuple contains the "i"th element of each array
print d

e= np.asarray(d)
print e

# arrays a, b, and c have now been organized into columns in a numpy array 