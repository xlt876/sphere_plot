#!/usr/bin/env python
# -*- coding: utf-8 -*-

###
### Sphere Plot (Golden Ratio)
###

import numpy as np
from matplotlib import pylab
from mpl_toolkits.mplot3d import Axes3D

def golden_ratio_xyz(n):
    golden_angle = np.pi * (3 - np.sqrt(5))
    theta = golden_angle * np.arange(n)
    z = np.linspace(1 - 1.0 / n, 1.0 / n - 1, n)
    radius = np.sqrt(1 - z * z)
    points = np.zeros((n, 3))
    
    # XYZ
    points[:,0] = radius * np.cos(theta)
    points[:,1] = radius * np.sin(theta)
    points[:,2] = z
    return points

def plot(points,save_png = True):
    #2Dfig to 3Dfig
    fig=pylab.figure()
    ax = Axes3D(fig)
     
    #axis label
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.scatter3D(points[:,0], points[:,1],points[:,2] ,color =(0.0,0.0,1.0),marker="o",s=5,label=u"Setosa")
    if save_png == True:
        pylab.savefig("sumpling_point.png", format = 'png' ,dpi=200)
    pylab.show()
    

if __name__ == '__main__':

    #Input Sampling Points
    n = int(raw_input('sampling_point='))
    n_points = golden_ratio_xyz(n)
    plot(n_points, False)
    
    




