# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:07:55 2018

@author: demetri
"""

import numpy as np
from numpy import zeros
import warnings
import scipy.misc
import time as time
import matplotlib.pyplot as plt
import matplotlib 
from matplotlib import animation
from random import randint
plt.rcParams['animation.ffmpeg_path'] = 'ffmpeg'

matplotlib.style.use('seaborn')

#sierpenski triangle
def middle(x,y,a,b):  #a and b set ratios
    return[a*(x[0]+y[0])/b,a*(x[1]+y[1])/b]
startime=time.time()
#initialize starting points
x1=[0,0]
x3=[1,0]
x2=[.5, np.sqrt(2)/2]    
current_point=[0,0]  
for i in range (400):
    number=randint(0,2)
    if number==0:
        current_point=middle(current_point, x1,1,2)
        #current_point=[0.5*(current_point[0]+x1[0]),0.5*(current_point[1]+x1[1])]
    if number==1:
        current_point=middle(current_point, x2,1,2)
        #current_point=[0.5*(current_point[0]+x2[0]),0.5*(current_point[1]+x2[1])]
    if number==2:
        current_point=middle(current_point, x3,1,2)
        #current_point=[0.5*(current_point[0]+x3[0]),0.5*(current_point[1]+x3[1])]
    plt.scatter(current_point[0], current_point[1], s=2, c='blue')
plt.show()
endtime=time.time()

print(format(endtime-startime))