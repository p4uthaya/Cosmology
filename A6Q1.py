# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 18:43:58 2017

@author: Prabha
"""

import numpy as np
import matplotlib.pyplot as plt


y,x=np.ogrid[0:3:100j,0:3:100j]

plt.contour(x.ravel(),y.ravel(),x-(2/3)*(((-(1-x-y)**3)/(3*y))**(1/2)),[0],colors =('k'))
plt.contour(x.ravel(),y.ravel(),1-x-y,[0],linestyles = 'dashed',colors = ('k'))
plt.title('Curvature and Expansion Types for  Matter + Lambda Universes', y = 1.05)
plt.xlabel('$\Omega$$_{m}$')
plt.ylabel('$\Omega$$_{\Lambda}$')
plt.savefig('1f.png', dpi = 1000)
