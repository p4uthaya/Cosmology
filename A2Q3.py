# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 22:27:11 2017

@author: Prabha
"""

import numpy as np


D = 30
R = 60
acc = ((R*R)*(np.sin(D/R))*(np.sin(D/R)))/(D*D)
count = 0


while acc < 0.95 :
    count += 1
    R = R + 0.0001
    if count == 10:
        print (acc, R)
        count = 0
    acc = ((R*R)*(np.sin(D/R))*(np.sin(D/R)))/(D*D)
    
print(acc,R)


    


