# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:47:07 2021

@author: Manav
"""

class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def add(self):
        return (self.x+self.y)
    def sub(self):
        return (self.x-self.y)
    def div(self):
        return (self.x/self.y)
    def mul(self):
        return (self.x*self.y)
    
        
x = int(input("Num 1 :- "))
y = int(input("Num 2 :- "))
calc1 = Calculator(x, y)

print(calc1.add())
print(calc1.sub())
print(calc1.mul())
print(calc1.div())
