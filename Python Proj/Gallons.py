# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:27:26 2020

@author: Manav
"""

 # Calculates time, gallons of gas used, and cost of gasoline for a trip
distance = eval(input("Enter the distance travelled in miles :- "))
mpg = float(input("Enter the miles travelled per gallon :-"))
speed = eval(input("Enter the speed of the car(mph) :- "))
costPerGallon = eval(input("Enter the cost per gallon(USD) :- "))

time = distance/speed
gallons = distance/mpg
cost = gallons*costPerGallon

print("Time taken:- ",time,"hrs")
print("Gallons of gas consumed:- ",gallons)
print("Cost of gasoline:- ",cost,"USD")