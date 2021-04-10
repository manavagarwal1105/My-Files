# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:08:38 2021

@author: Manav

"""

import numpy as np

def calc(x,y):
    x_arr = np.array(x) #converting a list into an array
    y_arr = np.array(y)
    x_mean = x_arr.mean() #Calculating the mean
    y_mean = y_arr.mean()
    n = len(x)
    
    #Calculating the covariance
    cov = 0
    for i in range(len(x)):
        cov += ((x_arr[i] - x_mean)*(y_arr[i] - y_mean))/n-1 

    return (x_mean,y_mean,cov)

a = calc([77, 50, 71, 72, 81, 94, 96, 99, 67],[82, 66, 78, 34, 47, 85, 99, 99, 68])
print(a)
