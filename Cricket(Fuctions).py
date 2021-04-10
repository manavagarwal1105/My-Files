
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:31:36 2020

@author: Manav
"""

#Cricket(TOURNAMENT) 

'''
The rules of this game are similar to that of a regular hand cricket, 
In order to take wicket, the number chosen by the bot and user should match.
The number should be from 1 to 10.
The winner of the toss will bat first.
The int value will depend on the match type
'''
from random import randint

#Defined Functions :-

def make_menu_square(str,z,l):
    a = len(str)+len(z)+len(l)
    print("*"*a)
    print("*",str,z,l,"*")
    print("*"," "*56,"*")
    print("*"*a)
"""
In toss, user will be asked to choose either even or odd Suppose the user chooses Even. 
If the sum of the integers chosen by user and bot is even, he/she wil win the toss same 
goes for odd as well.
"""
def toss(int):  
    a = randint(1,10)
    b = int
    c = a + b   
    return c
#--------------------------User's Innings----------------------------------
#In these functions, int represents the no.of playable balls
def user_bats_first(int):
    global user_runs1
    global user_balls1
    user_runs1= 0
    user_balls1 = 0
    print("Toss was won by", user_name,". He will bat first")
    for i in range(int):
        u = eval(input("hit's runs : -"))
        c = randint(1,10)
        if u != c:
            print(u,"runs in this ball")
            user_runs1 = user_runs1 + u
            user_balls1 += 1
        else:
            print("WICKET!")
            user_balls1 +=1
            break
        
def user_bats_second(int):
    global user_runs2
    global user_balls2
    user_runs2 = 0
    user_balls2 = 0
    out = False
    for i in range(int):
        while user_runs2 <= bot_runs1 and not(out):
            u = eval(input("hit's runs : -"))
            c = randint(1,10)
        
            if u != c:
                print(u,"runs in this ball")
                user_runs2 = user_runs2 + u
                user_balls2 += 1
            else:
                out = True
                print("WICKET!")
                user_balls2 += 1
                break
            break
#--------------------------Bots's Innings--------------------------------
def bot_bats_first(int):
    global bot_runs1
    global bot_balls1
    bot_runs1 = 0 
    bot_balls1 = 0
    for i in range(int):
        c =randint(1,10)
        u = eval(input("bowl : -"))
        if u != c:
            print(c,"runs in this ball")
            bot_runs1 = bot_runs1 + c
            bot_balls1 += 1
        else:
            print("OUT!")
            bot_balls1 += 1
            break
        
def bot_bats_second(int):
    global bot_runs2
    global bot_balls2
    bot_runs2 = 0 
    bot_balls2 = 0
    out = False
        
    for i in range(int):
        while bot_runs2 <= user_runs1 and not(out):
            c =randint(1,10)
            u = eval(input("bowl : -"))
        
            if u != c:
                print(c,"runs in this ball")
                bot_runs2 = bot_runs2 + c
                bot_balls2 += 1
            else:
                out = True
                print("OUT!")
                bot_balls2 += 1
                break
            break
#------------------------------------------------------------------------------
# The Menu
user_name = input("Enter your name : ")

intro = make_menu_square("Hi",user_name,"! Welcome to the ulimate cricket club. Hope you enjoy playing here.")
match_type = input("What would you like to play today?\nTest Match\nODI\nT20\n:-")
tm = "Test Match"
odi = "ODI"
t20 = "T20"
"""------------------------------------------------------------------------------"""

                           # Plays Test Match #

if match_type == tm:
    x = print("Nice choice. Since it is a testmatch, it will be of unlimited balls.\nYou better conserve your stamina and play smartly. ")
    print("Folks! Now its time to toss and decide who will bat first.")
    choose = input("Type E for even and O for Odd:")
    even = "E"
    odd = "O"
    
    #Toss
    q = int(input("Enter a number: "))
    z = toss(q)
    test_toss = print("The sum of numbers chosen by",user_name,"and bot is",z)
    
#In this case the user bats first :
    if choose == even:
        if z%2 == 0:
            user_bats_first(1000) #since its a test match,no.of balls is 1000
        
            print(user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

            print("The second innings start")
# Bot comes in to bat for 2nd inning   
            bot_bats_second(1000)
        
            print("bot has scored",bot_runs2,"in",bot_balls2,"balls")
            if user_runs1 > bot_runs2:
                print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
            elif user_runs1 < bot_runs2:
                print("BRAVO!THE BOT WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
 

#The bot bats in the first inning
        elif z%2 != 0:
            print("The toss was won by bot. The bot will bat first")
            bot_bats_first(1000)
            print("bot has scored",bot_runs1,"off",bot_balls1,"balls")
                
            print("Target is of",bot_runs1)

            print("The second innings start")
    
# The user comes in to bat for 2nd inning
            user_bats_second(1000)
            
            print("User has scored",user_runs2,"off",user_balls2,"balls")
    
            if user_runs2 > bot_runs1:
                print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
            elif user_runs2 < bot_runs1:
                print("BRAVO!THE BOT WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
# The user comes in to bat for 1st innings
    elif choose == odd:
        if z != 0:
            user_bats_first(1000)
        
            print(user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

            print("The second innings start")
# Bot comes in to bat for 2nd inning   
            bot_bats_second(1000)
        
            print("bot has scored",bot_runs2,"in",bot_balls2,"balls")
            if user_runs1 > bot_runs2:
                print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
            elif user_runs1 < bot_runs2:
                print("BRAVO!THE BOT WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
 

#The bot bats in the first inning
        elif z == 0:
            print("The toss was won by bot. The bot will bat first")
            bot_bats_first(1000)
            print("bot has scored",bot_runs1,"off",bot_balls1,"balls")
                
            print("Target is of",bot_runs1)

            print("The second innings start")
    
# The user comes in to bat for 2nd inning
            user_bats_second(1000)
            
            print("User has scored",user_runs2,"off",user_balls2,"balls")
    
            if user_runs2 > bot_runs1:
                print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
            elif user_runs2 < bot_runs1:
                print("BRAVO!THE BOT WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
                
                
#----------------------------------------------------------------------------#

                                # Plays ODI
elif match_type == odi:
    x = print("Nice choice captain. Since it is an ODI match, it will be of 50 overs.\nYou better conserve your stamina and play smartly. ")
    print("Folks! Now its time to toss and decide who will bat first.")
    choose = input("Type E for even and O for Odd:")
    even = "E"
    odd = "O"
        
    #Toss
    q2 = int(input("Enter a number: "))
    z2 = toss(q2)
    test_toss = print("The sum of numbers chosen by",user_name,"and bot is",z2)
    
#In this case the user bats first
    if choose == even:
        if z2%2 == 0:
            user_bats_first(300) #since its an ODI, playable balls = 300
            print(user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

            print("The second innings start")
# Bot comes in to bat for 2nd inning   
            bot_bats_second(300)
        
            print("bot has scored",bot_runs2,"in",bot_balls2,"balls")
            if user_runs1 > bot_runs2:
                print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
            elif user_runs1 < bot_runs2:
                print("BRAVO!THE BOT WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
 

#The bot bats in the first inning
    elif choose == even:
        if z2%2 != 0:
            
            bot_bats_first(300)
            print("bot has scored",bot_runs1,"off",bot_balls1,"balls")
    
            print("Target is of",bot_runs1)

            print("The second innings start")
    
# The user comes in to bat for 2nd inning
            user_bats_second(300)
            print("User has scored",user_runs2,"off",user_balls2,"balls")
    
            if user_runs2 > bot_runs1:
                print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
            elif user_runs2 < bot_runs1:
                print("BRAVO!THE BOT WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
 #In this case the user bats first
    elif choose == odd:
        if z2%2 != 0:
            user_bats_first(300)
            print(user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

            print("The second innings start")
# Bot comes in to bat for 2nd inning   
            bot_bats_second(300)
        
            print("bot has scored",bot_runs2,"in",bot_balls2,"balls")
            if user_runs1 > bot_runs2:
                print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
            elif user_runs1 < bot_runs2:
                print("BRAVO!THE BOT WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
 
#The bot bats in the first inning
    elif choose == odd:
        if z2%2 == 0:
            
            bot_bats_first(300)
            print("bot has scored",bot_runs1,"off",bot_balls1,"balls")
    
            print("Target is of",bot_runs1)

            print("The second innings start")
    
# The user comes in to bat for 2nd inning
            user_bats_second(300)
            print("User has scored",user_runs2,"off",user_balls2,"balls")
    
            if user_runs2 > bot_runs1:
                print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
            elif user_runs2 < bot_runs1:
                print("BRAVO!THE BOT WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
#-----------------------------------------------------------------------------#

                              # Plays T20
                              
elif match_type == t20:
    x = print("Smart move. Since it is a T20 match, it will be of 20 overs.\nYou better conserve play smartly and try to put up a decent score in less number of balls. ")
    print("Folks! Now its time to toss and decide who will bat first.")
    choose = input("Type E for even and O for Odd:")
    even = "E"
    odd = "O"
    
    #Toss
    q3 = int(input("Enter a number: "))
    z3 = toss(q3)
    test_toss = print("The sum of numbers chosen by",user_name,"and bot is",z3)
    
#In this case the user bats first
    if choose == even:
        if z3%2 == 0:
            user_bats_first(120) #since its a T20, Playable balls = 120
            
            print(user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

            print("The second innings start")
 # Bot comes in to bat for 2nd inning   
            bot_bats_second(120)
        
            print("bot has scored",bot_runs2,"in",bot_balls2,"balls")
            if user_runs1 > bot_runs2:
                print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
            elif user_runs1 < bot_runs2:
                print("BRAVO!THE BOT WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
 

#The bot bats in the first inning
        elif z3%2 != 0:
            bot_bats_first(120)
            print("bot has scored",bot_runs1,"off",bot_balls1,"balls")
    
            print("Target is of",bot_runs1)

            print("The second innings start")
    
# The user comes in to bat for 2nd inning
            user_bats_second(120)
            print(user_name," has scored",user_runs2,"off",user_balls2,"balls")
    
            if user_runs2 > bot_runs1:
                print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
            elif user_runs2 < bot_runs1:
                print("BRAVO!THE BOT WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
 
#The user bats first
    elif choose == odd:
        if z3%2 != 0:
            user_bats_first(120)
            
            print(user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

            print("The second innings start")
 # Bot comes in to bat for 2nd inning   
            bot_bats_second(120)
        
            print("bot has scored",bot_runs2,"in",bot_balls2,"balls")
            if user_runs1 > bot_runs2:
                print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
            elif user_runs1 < bot_runs2:
                print("BRAVO!THE BOT WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
 

#The bot bats in the first inning
        elif z3%2 == 0:
            bot_bats_first(120)
            print("bot has scored",bot_runs1,"off",bot_balls1,"balls")
    
            print("Target is of",bot_runs1)

            print("The second innings start")
    
# The user comes in to bat for 2nd inning
            user_bats_second(120)
            print(user_name," has scored",user_runs2,"off",user_balls2,"balls")
    
            if user_runs2 > bot_runs1:
                print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
            elif user_runs2 < bot_runs1:
                print("BRAVO!THE BOT WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
    
    
    
