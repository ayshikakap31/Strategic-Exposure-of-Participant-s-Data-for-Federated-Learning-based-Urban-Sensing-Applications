# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:25:29 2022

@author: Ayshika Kapoor
"""

# Calculate SNN density of each point
def density(x, eps, count):
    numPoints=0
    for temp1 in range(0,count):
        if x[temp1] >= eps:
            numPoints += 1
    return numPoints