# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 22:31:06 2021

@author: Manav
"""

import numpy as np
import pandas as pd

def calc(x,y):
    x_arr = np.array(x)
    y_arr = np.array(y)
    x_mean = np.mean(x_arr)
    y_mean = y_arr.mean()
    
    n = len(x)
#Variance
    v = 0
    for i in range(len(x)):
        v += (x_arr[i] - x_mean)**2
        var = v/(n-1)
#Covariance
    s = 0
    for i in range(len(x)):
        s += ((x_arr[i] - x_mean)*(y_arr[i] - y_mean))
        cov = s/(n-1)

        z = (x_mean,y_mean,cov)
    print("N:-",n,"\nMean of X :- ",z[0],"\nMean of Y :- ",z[1],"\nVariance of X :- ",var,"\nCov(X,Y) :- ",z[2])
#b-beta
    beta = cov/var
#a-Alpha
    alpha = y_mean - (beta*x_mean)
    print("y = ",alpha," + ",beta,"x")
#y_hat
    Y_hat = []
    for i in range(n):
        y_hat = (alpha + (beta*x_arr[i]))
        Y_hat.append(y_hat)
   # print(Y_hat)
#SSR
    SSR = 0
    for i in range(n):
        SSR += (y_arr[i] - Y_hat[i])**2
    print("SSR:- ",SSR)
#SST
    SST = 0
    for i in range(n):
        SST += (y_arr[i] - y_mean)**2
    print("SST:- ",SST)
#R 
    r_sq = (1 - (SSR/SST))
    print("r_sq: ",r_sq)
#Se
    Se = np.sqrt(SSR/(n-2))
    print("Se:- ",Se)
#Sxx
    Sxx = 0
    for i in range(n):
        Sxx += (x_arr[i] - x_mean)**2
    print("Sxx",Sxx)
#Sxy
    Sxy = 0
    for i in range(n):
        Sxy += (x_arr[i] - x_mean)*(y_arr[i] - y_mean)
    print("Sxy",Sxy)
#Sb
    Sb = Se/np.sqrt(Sxx)
    print("Sb:- ",Sb)
#b
    b =Sxy/Sxx
    print("b:- ",b)
#t
    t = b/Sb
    print("t:- ",t)
a = calc([2024,      5038 ,       905,      3572,         1157,           327,      378,      191
],
  [ 1.90,       3.96 ,       2.44,       0.88,           0.37,        20.90,      0.49,      1.01
])