# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 09:50:57 2018

@author: demetri
"""

import numpy as np
from numpy import zeros
import warnings
import scipy.misc
import matplotlib.pyplot as plt
import matplotlib 
from matplotlib import animation
import random
import time
import math
import pandas as pd


plt.rcParams['animation.ffmpeg_path'] = 'ffmpeg'

matplotlib.style.use('fivethirtyeight')



#standard map
startime=time.time()


def standardmap(p, theta, K):  #defining the function
    plist=[]
    thetalist=[]
    for i in range(1000):  #1000 runs for each point
          #start with K-value of whatever
        pnew=(p+K*np.sin(theta))%(2*np.pi)
        thetanew=(theta+pnew)%(2*np.pi)
        
        p, theta=pnew, thetanew
        plist.append(p)
        thetalist.append(theta)
    return(thetalist, plist)  #we want to return 1000 values 
    
def func(x,y):
    return(x,y)
p_range=np.linspace(0,np.pi*2, 1000)
theta_range=np.linspace(0,np.pi*2,150)  #theta points 
#p,theta=np.meshgrid(p_range,theta_range)

K_range=np.linspace(0,1,100)
thetagraph=[]

pgraph=[]
#for k in K_range:  #plotting for different values of K
graphlist=[]
for j in theta_range:
    p=random.uniform(0,2*np.pi)#p_range[j]  
    theta=random.uniform(0,2*np.pi)#theta_range[j]
    graph=standardmap(p, theta, 1.5)
    graphlist.append(standardmap(p, theta, j))
    
    #thetagraph.append(j)
    #pgraph.append(standardmap(random.uniform(0,2*np.pi),random.uniform(0,2*np.pi), 0)[1])
    #graph 1000 points of both axes of phase diagram
    plt.scatter(graph[0], graph[1], s=.1)#plot 1000 points for each phase diagram point
    plt.savefig('standard%s.png'%j)
plt.show()    


endtime=time.time()

print(format(endtime-startime))




