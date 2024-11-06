# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:29:39 2022

@author: Ayshika Kapoor
"""
from findCoreNeighbors import findCoreNeighbors
def expandCluster(labels,neighborCore,corePts,C,sharednearestNeighbors,eps,visited):
    while len(neighborCore)>0:
            p=neighborCore.pop(0)
            if p in visited:
                continue
            labels[p]=C
            visited.append(p)
            neighCore=findCoreNeighbors(p,corePts,sharednearestNeighbors,eps)
            neighborCore.extend(neighCore)
    return labels