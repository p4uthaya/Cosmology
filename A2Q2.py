# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 12:48:20 2017

@author: Prabha
"""
import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
R = 6400
i = 0.01
r1 = R*i
r2 = R*np.sin(i)
diff = abs(r1-r2)
count = 0

while diff >= 1e-5/(2*pi) :
    count += 1
    i = i- diff/R
    r1 = R*i
    r2 = R*np.sin(i)
#    if count == 10:
#        print (r1)
#        count = 0
    diff = abs(r1-r2)

if diff < 1e-5/(2*pi):
    print(r1)
    print(r2)
    print(2*pi*r1)
    print(2*pi*r2)

