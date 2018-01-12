# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:06:33 2018


Code for making figures similar to those used in the board game "Prime Climb". 

I recommed the game too. I bought a copy.


@author: aslak
"""



import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy
import sympy

#primecolors={
# 2: 'xkcd:red', 3: 'xkcd:green', 5: 'xkcd:yellow', 7: 'xkcd:blue',
# 11: 'xkcd:lime green', 13: 'xkcd:brown', 17: 'xkcd:purple', 19: 'xkcd:teal',
# 23: 'xkcd:cyan', 29: 'xkcd:magenta', 31: 'xkcd:orange', 37: 'xkcd:olive',
# 41: 'xkcd:violet', 43: 'xkcd:dark green', 47: 'xkcd:pink', 
# 'fallback': '#808080',
#'background': '#000000',
#'text': '#FFFFFF',
#'spiral': '#808080',
#'board': '#000000'}

primecolors={ #based on https://sashat.me/2017/01/11/list-of-20-simple-distinct-colors/
              # and optimized using http://vrl.cs.brown.edu/color
2: "#e71d4c", 3: "#3ab44b", 5: "#fde019", 7: "#0482c7", 11: "#f58231", 13: "#901eb3", 17: "#46f0ef", 19:"#f134e8", 
23: "#3524f9", 29: "#007f7f", 31: "#964826", 37: "#adc16d", 41: "#fabdbe", 43: "#aef815", 47: "#442767",
'fallback': '#808080',
'background': '#000000',
'text': '#EEEEEE',
'spiral': '#808080',
'board': '#000000'}

#primecolors={ #based on the board game
#1: '#D1D3D4', 2: '#F2A243', 3: '#87C65F', 5: '#5DCBF0', 7: '#8E7DBA',
#'fallback': '#EB5F4C', 'background': '#FFFFFF', 'text': '#424243', 'spiral': '#FFFFFF',
#'board': '#424243'}

def drawnumber(xo,yo,num):
    if num == 1:
        factors = [1]
    else:
        factors = sympy.factorint(num)
        factors = list(sympy.utilities.iterables.multiset_combinations(factors, sum(factors.values())))[0]

    factors=factors[0::2] + factors[1::2]

    for ix,f in enumerate(factors):
        theta1 = 90+360*(ix-.5)/len(factors)
        theta2 = 90+360*(ix+.5)/len(factors)
        color = primecolors.get(f)
        if not color: 
            color = primecolors.get("fallback")
        p = patches.Wedge(center=(xo,yo), r=0.5, theta1=0, theta2=360, 
                          edgecolor="none", facecolor=primecolors.get('background'), linewidth=0);
        plt.gca().add_patch(p)
        p = patches.Wedge(center=(xo,yo), r=1.0, theta1=theta1, theta2=theta2, width=0.5, 
                          edgecolor=primecolors.get('background'), facecolor=color, linewidth=1)
        plt.gca().add_patch(p)
        
        plt.text(xo-0.01,yo-0.03, "{}".format(num),horizontalalignment='center',verticalalignment='center', 
                 color=primecolors.get('text'), weight='bold', size=12.0)
        if (f>110) & (len(factors)>1):
            theta = (theta1+theta2)*.5
            plt.text(xo+numpy.cos(theta*numpy.pi/180)*.75,yo+numpy.sin(theta*numpy.pi/180)*.75, 
                     f, horizontalalignment='center',verticalalignment='center', fontsize=5,
                     color=primecolors.get('text'))
            


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


def ulam(jmax): #https://www.youtube.com/watch?time_continue=1&v=iFuR97YcSLM
    taken = numpy.zeros((30,30))
    p = (15,15)
    v = (1,0)
    for jj in numpy.arange(1,jmax+1):
        drawnumber(p[0]*2.2,p[1]*2.2,jj)
        taken[p[0],p[1]] = 1
        vleft=(v[1],-v[0])
        if taken[p[0]+vleft[0],p[1]+vleft[1]]==0:
            v=vleft
        p = (p[0]+v[0],p[1]+v[1]) 

def justprimes():
    p=[1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    for ix,jj in enumerate(p):
        xo = (ix%4)*2
        yo = (ix/4)*2
        drawnumber(xo,yo,jj)


fig = plt.figure(facecolor=primecolors['board'],figsize=(8, 8), dpi=80)
ax1 = plt.Axes(fig, [0., 0., 1., 1.])
ax1.set_axis_off()
fig.add_axes(ax1)
ax1.axis('off')

#spiral()
square(10)
#ulam(100)
#justprimes()

ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.axis('tight')
ax1.axis('equal')

if False:
    plt.show()
else:
    fig.savefig('square.pdf', facecolor=primecolors['board'], edgecolor=primecolors['board'],
        orientation='portrait', pad_inches=0,
        frameon=None)
