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
'''
A=[]
mat=[[0.0,0.0,0.0,0.16,0.0,0.0,0.01],
[0.85,0.04,-0.04,0.85,0.0,1.6,0.85],
[0.2,-0.26,0.23,0.22,0.0,1.6,0.07],
[-0.15,0.28,0.26,0.24,0.0,0.44,0.07]]
x=0.0
y=0.0
for k in range(0,100000):
    p=random.random()
    if p <= mat[0][6]:
        i=0
    elif p <= mat[0][6] + mat[1][6]:
        i=1
    elif p <= mat[0][6] + mat[1][6] + mat[2][6]:
        i=2
    else:
        i=3

    x0 = x * mat[i][0] + y * mat[i][1] + mat[i][4]
    y  = x * mat[i][2] + y * mat[i][3] + mat[i][5]
    x = x0

    ptn=[x,y]

    A.append(ptn)

plt.figure(figsize=(20,30))
plt.scatter( *zip(*A),marker='o', color='g',s=0.1)
plt.show()
#really cool fern
'''

