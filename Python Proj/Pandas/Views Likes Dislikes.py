# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 11:56:59 2021

@author: Manav
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Manav/OneDrive/Desktop/SP JAIN/Others/All Projects/Python Proj/Pandas/CAvideos.csv",
                 index_col = 0)
a = df.head(5)
#b = a.plot()

#Line
plt.figure(figsize =(26,13), facecolor = "Orange")
plt.plot(a.index,a[["views","likes","dislikes"]])
plt.title("Views-Likes-Dislikes")
plt.xlabel("Songs")
plt.ylabel("Count in billions")
plt.show()

#Box Plot
a.plot(kind='box', subplots=True, layout=(2,2),sharex=False, sharey=False)
plt.show()

#Histogram
plt.figure(figsize =(16,9))
plt.hist(a)
plt.title("Views-Likes-Dislikes")
plt.xlabel("Count in billions")
plt.ylabel("Frequency")

#Hist Alt
r= a.plot(kind='hist', subplots=True, layout=(2,2),sharex=False, sharey=False)
print(r)