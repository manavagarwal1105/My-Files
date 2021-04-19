# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:32:02 2021

@author: Manav
"""
"""
This program reads a dataset of 41k youtube videos. It generates a sample dataset of 5 videos at random and visualize them by plotting, Line graph, Box Plot and Histogram
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import *

#The DataFrame
df = pd.read_csv("C:/Users/Manav/OneDrive/Desktop/SP JAIN/Others/All Projects/Python Proj/Pandas/CAvideos.csv")

#Sample DataFrame
ran = []
for i in range(5):
    z = randint(0,40881)
    ran.append(z)
a = ran

b = df.iloc[a]
b.set_index("title",inplace = True)

#Line Plot
plt.figure(figsize =(26,13), facecolor = "Orange")
plt.plot(b)
plt.title("Views-Likes-Dislikes")
plt.xlabel("YouTube Videos")

plt.show()

#Box Plot
b.plot(kind='box', subplots=True, layout=(2,2),sharex=False, sharey=False)
plt.show()

#Histogram
plt.figure(figsize =(16,9))
plt.hist(b)
plt.title("Views-Likes-Dislikes")
plt.xlabel("Count in billions")
plt.ylabel("Frequency")

#Hist Alt
r= b.plot(kind='hist', subplots=True, layout=(2,2),sharex=False, sharey=False)
print(r)
   
