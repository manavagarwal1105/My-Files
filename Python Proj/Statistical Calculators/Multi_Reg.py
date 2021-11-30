# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 13:21:53 2021

@author: Manav
"""
import numpy as np
import pandas as pd
def multi_reg(l2,l3,l4):
#Reg Eq
    df1 = pd.DataFrame({"x0" : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        "x1": l2,
        "x2":l3})

    df2 = pd.DataFrame({"y":l4})

    X = np.array(df1)
    Y = np.array(df2)

    X_T = np.transpose(X)
    Y_T = np.transpose(Y)

    A = np.matmul(X_T,X)
    A_inv = np.linalg.inv(A)

    B = np.matmul(A_inv,X_T)
    beta = np.matmul(B,Y)
    
    print("B1: ",beta[0],"B2: ",beta[1],"B3:",beta[2])
#SSR
    Y_hat = np.matmul(X,beta)
    SSR = 0
    for i in range(len(Y)):
        SSR += (Y[i] - Y_hat[i])**2
    print("SSR:- ",SSR)
#SST
    Y_mean = np.mean(Y)
    SST = 0
    for i in range(len(Y)):
        SST += (Y[i] - Y_mean)**2
    print("SST:- ",SST)
#R 
    r = np.sqrt(1 - (SSR/SST))
    print("r: ",r)
#Se
    n = len(X)
    Se = np.sqrt(SSR/(n-2))
    print("Se:- ",Se)
    
    
multi_reg(
          [410,368,357,373,361,385,380,400,407,410,421,446,478,441,454,440,427],
          [9,11,15,12,9,9,10,12,12,13,12,19,19,18,12,12,12],
          [776,580,539,648,538,891,673,783,571,627,727,867,1042,804,832,764,727])