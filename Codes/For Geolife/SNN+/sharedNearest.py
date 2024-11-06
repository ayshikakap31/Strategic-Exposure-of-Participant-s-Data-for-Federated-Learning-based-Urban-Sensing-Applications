# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:25:09 2022

@author: Ayshika Kapoor
"""
import numpy as np
# Function to construct Shared Nearest Neighbor graph from sparsified matrix
def countIntersection(list_1,list_2):
    intersection = 0
    for temp1 in list_1:
        if temp1 in list_2:
            intersection += 1
    return intersection

def sharedNearest(count,k,similarityMatrix):
    SNNgraph = np.zeros((count,count))
    for temp1 in range(0,count-1):
        nextIndex = temp1+1
        for temp2 in range(nextIndex, count):
            if temp2 in similarityMatrix[temp1] and temp1 in similarityMatrix[temp2]:
                count1=countIntersection(similarityMatrix[temp1], similarityMatrix[temp2])
                SNNgraph[temp1,temp2] = count1
                SNNgraph[temp2,temp1] = count1
    return SNNgraph