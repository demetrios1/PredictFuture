# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:07:09 2018

@author: demetri
"""
from PIL import Image
import numpy as np
from numpy import zeros
import warnings
import scipy.misc
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib 
import time
from matplotlib import animation
from random import randint
plt.rcParams['animation.ffmpeg_path'] = 'ffmpeg'

matplotlib.style.use('ggplot')

startime=time.time()

#arnolds cat



#changed the picture size
image=np.array(Image.open('folespic.jpg'))  #200x200
imageinit=np.array(Image.open('folespic.jpg'))
image2=Image.open('pic2.jpg')
def changesize(x):
    imagenew=Image.open('pic2.jpg')  #using the default jonah hill pic
    imagenew=np.array(imagenew.resize((x,x)))
    imageinit=imagenew
    return(imagenew, imageinit)

xlen=image.shape[0]
ylen=image.shape[1]
#empty grid
empty=np.zeros([xlen, ylen], int)
#x=np.linspace(0,N, N+1)
#y=np.linspace(0,N,N+1)
#map grid
X,Y=np.meshgrid(range(xlen),range(ylen))
#functions
xnew=(2*X+Y)%xlen
ynew=(X+Y)%ylen


def difference(picture1, picture2):
	dif = np.sum(picture1 - picture2)
	
	return(dif)
'''
count=0

        
fig = plt.figure() # make figure
ax = fig.add_subplot(111)
time_text = ax.text(.85, 1.05, '', transform=ax.transAxes, fontsize=20)
pictures=[]
for i in range(121):
    new=Image.fromarray(image)
    image=image[xnew,ynew]
    
    pictures.append(new)
    
    if difference(image,imageinit)!=0:
        count+=1
    else:
        print('Done it took %s times' %count)


# make axesimage object
# the vmin and vmax here are very important to get the color map correct

im=plt.imshow(pictures[0], cmap=plt.get_cmap('jet'), vmin=0, vmax=255, animated=True)

# function to update figure
def updatefig(j):
    # set the data in the axesimage object
    im.set_array(pictures[j])
    time_text.set_text(r'count = %d ' % (j))
    # return the artists set
    return [im]
# kick off the animation
plt.xticks([])
plt.yticks([])
ani=animation.FuncAnimation(fig, updatefig, frames=121, blit=True)

mywriter = animation.FFMpegWriter()
ani.save('animation.mp4', writer=mywriter)
plt.show()
'''


def get_count(image, imageinit):
    count=0
    xlen=image.shape[0]
    ylen=image.shape[1]
    X,Y=np.meshgrid(range(xlen),range(ylen))
    xnew=(2*X+Y)%xlen
    ynew=(X+Y)%ylen
    for i in range (xlen):
        new=Image.fromarray(image)
        image=image[xnew,ynew]
        if difference(image,imageinit)!=0:
            count+=1
        else:
            break
    return(count+1)

xlist=[]
ylist=[]

#plotting a bunch of different sizes

for i in range (1,400):
    a,b=changesize(i)
    ylist.append(get_count(a,b))  #count
    xlist.append(i)  #size of grid
    #plt.plot(xlist, ylist,'bo')
    #plt.xlabel('NxN grid size', fontsize=16)
    #plt.ylabel('Iterations', fontsize=16)
    #plt.title('Number of times to reach original pic vs pixel size', fontsize=14)
plt.hist(ylist, histtype='bar', bins=30,alpha=0.75, ec='black',  linewidth=1.1, stacked=True, normed=True)#  histtype='bar', ec='black', linewidth=1.3,alpha=0.5, align='left')# color=color[i],
sns.kdeplot(ylist, shade=True)
#plt.xticks(np.arange(min(xlist), max(xlist), 25.0))
   
plt.show()

endtime=time.time()

print(format(endtime-startime))