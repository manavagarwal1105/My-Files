# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 23:15:33 2021

@author: Manav
"""

class Investment:
    def __init__(self,p,i,n): #p is principal amnt, i  interest, n = duration
        self.p = p
        self.i = i
        self.n = n
    def value_after(self):
        return self.p*(1+self.i)**self.n
    def __str__(self):
        return ("Principal Amt: {}  Interest: {}  Duration: {}").format(self.p,self.i,self.n)
    
details = Investment(1000,10,2)
print("The value would be : ",details.value_after())
print(details)