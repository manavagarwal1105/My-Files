# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:54:15 2020

@author: Manav
"""
#Used to guess password
password = "MANAV"
guess = ""


guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != password and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the password :- ")
        guess_count += 1
    else:
        out_of_guesses = True
        
if out_of_guesses:
    print("Kicked off the system ")
    
else:
    print("You are welcome")
    
    