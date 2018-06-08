#!/usr/bin/env python  
#encoding: utf-8  
    
from pylab import *  
from mpl_toolkits.mplot3d import Axes3D  
    
fig = figure()  
ax = Axes3D(fig)  
X = np.arange(-4, 4, 0.25)  
Y = np.arange(-4, 4, 0.25)  
X, Y = np.meshgrid(X, Y)  
R = np.sqrt(X**2 + Y**2)  
Z = np.sin(R)  
    
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.hot)  
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=cm.hot)  
ax.set_zlim(-2, 2)  
    
savefig('figure/plot3d_ex.png', dpi=48)  
show()  