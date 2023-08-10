#pi estimation
import numpy as np
import random
import matplotlib as mpl
from matplotlib import pyplot as plt, patches

circle_points=0
square_points=0
interval=20

fig = plt.figure()
ax = fig.add_subplot(111)
rect = patches.Rectangle((-1,-1), 2, 2, color='pink')
circle = patches.Circle((0,0), radius=1, color='skyblue')
ax.add_patch(rect)
ax.add_patch(circle)

x=[]
y=[]
for i in range(interval**2):
    x_rand=random.uniform(-1,1)
    x.append(round(x_rand,3))
    y_rand=random.uniform(-1,1)
    y.append(round(y_rand,3))

    dist=x_rand**2 + y_rand**2
    if dist<=1:
        circle_points=circle_points+1
    square_points=square_points+1

pi=(4*circle_points)/square_points
ax.scatter(x,y,color="red",alpha=0.5,s=1)
plt.axis('equal')
plt.show()
print("Estimated value of PI is ",pi)
