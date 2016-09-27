# Chapter Three Exercise Three

import numpy as np
h_initial= 10                     #initial height, h is defined as 10 meters
g= 9.8                         # acceleration due to gravity, g, is defined as 9.8 m/s^2
y= np.arange(10.0, 0.0, -0.5)  # Defines position y as an array of distances from 10m to 0m with increments of 0.5
t=(2.0*(h_initial-y)/g)**(0.5) #definse time, t, for a falling object when distance changes in time
print t                        #prints t