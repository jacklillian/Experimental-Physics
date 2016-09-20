# Quadratic Formula
import numpy as np
a=1
a= a+0j
b=2
b= b+0j
c=4
c= c+0j
numpos= -b + np.sqrt((b**2.0)-(4.0*a*c))
numneg= -b - np.sqrt((b**2.0)-(4.0*a*c)) 
denom = 2.0*a
xpos= numpos/denom
xneg= numneg/denom
print xpos
print xneg
