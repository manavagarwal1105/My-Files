# -*- coding: utf-8 -*-

"""
Created on Mon Apr  5 22:49:17 2021

@author: Manav
"""
"""
Creating a function named `calculate()` in `mean_var_std.py` that uses Numpy to 
output the mean, variance, standard deviation, max, min, and sum of the rows, 
columns, and elements in a 3 x 3 matrix.
"""
import numpy as np
from array import *

def calculate(list):
    arr = np.array(list).reshape(3,3)
    
    mean_col = np.mean(arr, axis = 0)
    l_mean_col = mean_col.tolist()
    mean_row = np.mean(arr, axis = 1)
    l_mean_row = mean_row.tolist()
    mean_arr = np.mean(arr)
    l_mean_arr = mean_arr.tolist()
    l_mean = [l_mean_col, l_mean_row, l_mean_arr]
    mean = ("Mean :-",l_mean)
    mean_str = "".join(map(str,mean))
    
    std_col = np.std(arr, axis = 0)
    l_std_col = std_col.tolist()
    std_row = np.std(arr, axis = 1)
    l_std_row = std_row.tolist()
    std_arr = np.std(arr)
    l_std_arr = std_arr.tolist()
    l_std = [l_std_col,l_std_row,l_std_arr]
    std = ("Std Deviation: ",l_std)
    std_str = "".join(map(str,std))
    
    var_col = std_col**2
    l_var_col = var_col.tolist()
    var_row = std_row**2
    l_var_row = var_row.tolist()
    var_arr = std_arr**2
    l_var_arr = var_arr.tolist()
    l_var = [l_var_col,l_var_row,l_var_arr]
    var = ("Variance:- ", l_var)
    var_str = "".join(map(str,var))
    
    max_col = np.max(arr,axis = 0)
    l_max_col = max_col.tolist()
    max_row = np.max(arr, axis = 1)
    l_max_row = max_row.tolist()
    max_arr = np.max(arr)
    l_max_arr = max_arr.tolist()
    l_max = [l_max_col,l_max_row,l_max_arr]
    maxi = ("Maximum:- ",l_max)
    maxi_str = "".join(map(str,maxi))
    
    min_col = np.min(arr,axis = 0)
    l_min_col = min_col.tolist()
    min_row = np.min(arr, axis = 1)
    l_min_row = min_row.tolist()
    min_arr = np.min(arr)
    l_min_arr = min_arr.tolist()
    l_min = [l_min_col,l_min_row,l_min_arr]
    mini = ("Minimum:- ",l_min)
    mini_str = "".join(map(str,mini))
    
    print(mean_str)
    print(var_str)
    print(std_str)
    print(maxi_str)
    print(mini_str)
      
a= calculate([0.103,0.072,0.071,0.077,0.086,0.047,0.060,0.050,0.070])
