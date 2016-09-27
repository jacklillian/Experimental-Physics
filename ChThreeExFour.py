# Chapter Three Exercise Four

import numpy as np
h_initial= 10                     #initial height, h is defined as 10 meters
g= 9.8                         # acceleration due to gravity, g, is defined as 9.8 m/s^2
y= np.arange(10.0, 0.0, -0.5)  # Defines position y as an array of distances from 10m to 0m with increments of 0.5
t=(2.0*(h_initial-y)/g)**(0.5) #definse time, t, for a falling object when distance changes in time
print t                        #prints t

# The calculations from the previous exercise will be used in this calculation

delta_y= y[1:20]-y[0:19]    # defines the change in position of the particle over the time interval
delta_t= t[1:20]-t[0:19]    # defines the changes between moments when the ball passes each 0.5m interval 
v = delta_y/delta_t         # defines the average velocity as the change in position over the change in time
print v                     # prints the average velocity over the intervals as an array