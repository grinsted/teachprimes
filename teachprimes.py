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
 47: 'xkcd:pink',
'fallback': '#808080',
'background': '#000000',
'text': '#FFFFFF',
'spiral': '#808080'}

primecolors={ #based on https://sashat.me/2017/01/11/list-of-20-simple-distinct-colors/
              # and optimized using http://vrl.cs.brown.edu/color
2: "#e71d4c", 3: "#3ab44b", 5: "#fde019", 7: "#0482c7", 11: "#f5812f", 13: "#901eb3", 17: "#46f0ef", 19:"#f134e8", 
23: "#2524f9", 29: "#007f7f", 31: "#ab6f28", 37: "#a8fec1", 41: "#37216c", 43: "#aef815", 47: "#fabdbe",
'fallback': '#808080',
'background': '#000000',
'text': '#FFFFFF',
'spiral': '#808080'}

#primecolors={ #based on the board game
#1: '#D1D3D4', 2: '#F2A243', 3: '#87C65F', 5: '#5DCBF0', 7: '#8E7DBA',
#'fallback': '#EB5F4C', 'background': '#FFFFFF', 'text': '#424243', 'spiral': '#FFFFFF'}

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
            color = primecolors.get("fallback")
        p = patches.Wedge(center=(xo,yo), r=0.5, theta1=0, theta2=360, 
                          edgecolor="none", facecolor=primecolors.get('background'), linewidth=0);
        plt.gca().add_patch(p)
        p = patches.Wedge(center=(xo,yo), r=1.0, theta1=theta1, theta2=theta2, width=0.5, 
                          edgecolor=primecolors.get('background'), facecolor=color, linewidth=1)
        plt.gca().add_patch(p)
        
        plt.text(xo,yo, "{}".format(num),horizontalalignment='center',verticalalignment='center', 
                 color=primecolors.get('text'))
#        if f>11:
#            theta = (theta1+theta2)*.5
#            plt.text(xo+numpy.cos(theta*numpy.pi/180)*.75,yo+numpy.sin(theta*numpy.pi/180)*.75, 
#                     f, horizontalalignment='center',verticalalignment='center', fontsize='x-small',
#                     color=primecolors.get('text'))
            


def spiral():
    jmax = 101
    
    afun = lambda jj: numpy.sqrt(((jmax+1-jj)/jmax)) #angle
    rfun = lambda jj: afun(jj)*15.0 #radius
    xfun = lambda jj: numpy.multiply(rfun(jj), numpy.cos(afun(jj)*11.0*numpy.pi))
    yfun = lambda jj: numpy.multiply(rfun(jj), numpy.sin(afun(jj)*11.0*numpy.pi))
    
    jj = numpy.linspace(1,jmax,2000)
    plt.plot(xfun(jj),yfun(jj), color=primecolors['spiral'],zorder=-10, linewidth=2)
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

spiral()


ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.axis('tight')
ax1.axis('equal')
plt.show()

