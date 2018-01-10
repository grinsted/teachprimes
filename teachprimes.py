# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:06:33 2018


Code for making figures similar to those used in the board game "Prime Climb". 




@author: aslak
"""



import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy
import sympy

primecolors={
 2: 'xkcd:red',
 3: 'xkcd:green',
 5: 'xkcd:yellow',
 7: 'xkcd:blue',
 11: 'xkcd:lime green',
 13: 'xkcd:brown',
 17: 'xkcd:purple',
 19: 'xkcd:teal',
 23: 'xkcd:cyan',
 29: 'xkcd:magenta',
 31: 'xkcd:orange',
 37: 'xkcd:olive',
 41: 'xkcd:violet',
 43: 'xkcd:dark green',
 47: 'xkcd:pink'}

primecolors={ #based on https://sashat.me/2017/01/11/list-of-20-simple-distinct-colors/
2: '#E6194B',
3: '#3CB44B',
5: '#FFE119',
7: '#0082C8',
11: '#F58230',
13: '#911EB4',
17: '#46F0F0',
19: '#F032E6',
23: 'xkcd:lime green',
29: '#FABEBE',
31: '#008080',
37: '#AA6E28',
41: '#FFFAC8',
43: '#AAFFC3',
47: '#808000'}

def drawnumber(xo,yo,num):
    if num == 1:
        factors = [1]
    else:
        factors = sympy.factorint(num)
        factors = list(sympy.utilities.iterables.multiset_combinations(factors, sum(factors.values())))[0]

    for ix,f in enumerate(factors):
        theta1 = 360*ix/len(factors)
        theta2 = 360*(ix+1)/len(factors)
        color = primecolors.get(f)
        if not color: 
            color = '#808080'
        p = patches.Wedge(center=(xo,yo), r=0.5, theta1=0, theta2=360, 
                          edgecolor="none", facecolor="#000000", linewidth=0);
        plt.gca().add_patch(p)
        p = patches.Wedge(center=(xo,yo), r=1.0, theta1=theta1, theta2=theta2, width=0.5, 
                          edgecolor="#000000", facecolor=color, linewidth=1)
        plt.gca().add_patch(p)
        
        plt.text(xo,yo, "{}".format(num),horizontalalignment='center',verticalalignment='center',color="#FFFFFF")          


def spiral():
    jmax = 101
    
    afun = lambda jj: numpy.sqrt(((jmax+1-jj)/jmax)) #angle
    rfun = lambda jj: afun(jj)*14.0 #radius
    xfun = lambda jj: numpy.multiply(rfun(jj), numpy.cos(afun(jj)*11.0*numpy.pi))
    yfun = lambda jj: numpy.multiply(rfun(jj), numpy.sin(afun(jj)*11.0*numpy.pi))
    
#    jj = numpy.linspace(1,jmax,2000)
#    plt.plot(xfun(jj),yfun(jj), 'w')
    for jj in numpy.arange(1,jmax+1):
        drawnumber(xfun(jj),yfun(jj),jj)
    

def square(n=10):
    jmax = n*n
    
    xfun = lambda jj: ((jj-1) % 10)*2.2
    yfun = lambda jj: numpy.floor((jj-1)/10.0)*2.2
    
    for jj in numpy.arange(1,jmax+1):
        drawnumber(xfun(jj),yfun(jj),jj)


fig = plt.figure(facecolor='black')
ax1 = plt.Axes(fig, [0., 0., 1., 1.])
ax1.set_axis_off()
fig.add_axes(ax1)
ax1.axis('off')

square(10)


ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.axis('tight')
ax1.axis('equal')
plt.show()

