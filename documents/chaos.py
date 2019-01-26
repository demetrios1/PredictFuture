# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 20:40:50 2017

@author: Demetri
"""
import seaborn as sn
import turtle
import numpy as np
import random
import pylab
import matplotlib.pyplot as plt
from random import randint
import time
startTime = time.time()
def midpoint(point1, point2):
    return [3*(point1[0] + point2[0])/8, 3*(point1[1] + point2[1])/8]

current_point = [0,0]  # our seed value for the chaos game
                    # It can fall anywhere inside the triangle

# our equilateral triangle vertices
v1 = [0,0]
v2 = [1,0]
v3 = [0,1]
v4 = [1,1]
#v5= [.5,1.5]
# Plot x number of  points
#plt.ion()
for  number in range(10000):
    # choose a triangle vertex at random
    # set the current point to be the midpoint
    # between the previous current point and
    # the randomly chosen vertex, 1 goes to  vert, 2 to other, 0 to other, 3 to corner
    value = randint(0,4)
    if value == 0:
        current_point = midpoint(current_point, v1)
    if value == 1:
        current_point = midpoint(current_point, v2)
    if value == 2:
        current_point = midpoint(current_point, v3)
    if value==3:
        current_point = midpoint(current_point, v4)
    #if value==4:
     #   current_point=midpoint(current_point, v5)
    #plt.pause(0.001)
    # plot the new current point
    pylab.plot(current_point[0],current_point[1],'b.',markersize=3.5)
   
    #plt.xlim(-.2,1)
    #plt.ylim(-.1,.5)
pylab.show()


endTime = time.time()
print("Execution time: {:.1f} seconds".format(endTime - startTime))


