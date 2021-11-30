# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:57:40 2020

@author: Manav
"""
"""
A program which calculates the final amount emaining after gambling 1000
times.
If we win once, we get 36 USD and if we loose once, we have to pay 1 USD
"""
from random import randint

win = 0
loss = 0

for i in range(10000):
    my_number = randint(0,36)
    winning_number = randint(0,36)
    
    if my_number == winning_number:
        win = win + 1
       
    else:
        loss = loss + 1
        
    
profit = 36*win
losses = 1*loss

final = profit - losses
print(final)
