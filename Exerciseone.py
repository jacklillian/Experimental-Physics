# Calculates height and velocity of thrown ball
inHeight = 1.2          # meters
inVelocity = 5.4        # meters/sec
g = 9.8                 # acc. due to grav. m/s^2
time = 2.0             # seconds
height = inHeight + inVelocity*time -(1/2)*g*(time**2)
velocity = inVelocity - g*time