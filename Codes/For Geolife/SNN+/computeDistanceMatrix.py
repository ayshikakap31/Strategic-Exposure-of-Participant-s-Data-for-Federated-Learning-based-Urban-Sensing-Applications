# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:22:18 2022

@author: Ayshika Kapoor
"""
import numpy as np
# To compute Spatial-Temporal Distance
def eucledian_dist(lat1,lon1,time1,lat2, lon2,time2):
    return ((0.5*(abs(float(lat2)-float(lat1))**2+abs(float(lon2)-float(lon1))**2)**0.5)+(0.5*abs(float(time2)-float(time1))))
# Function to compute pairwise distance
def computeDistanceMatrix(latitude,longitude,timeHour):
    #distanceMatrix=[[0 for i in range(len(latitude))] for j in range(len(latitude))]
    distanceMatrix = np.zeros(( len(latitude), len(latitude) ))
    for temp1 in range(len(latitude)):
        for temp2 in range(len(longitude)):
            distanceMatrix[temp1][temp2] = eucledian_dist(latitude[temp1], longitude[temp1],timeHour[temp1], latitude[temp2], longitude[temp2], timeHour[temp2])
    return distanceMatrix