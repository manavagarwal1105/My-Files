# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 01:55:17 2021

@author: Manav
"""

#CRICKET(TEAM 3.0)

"""
Added feature :- SCORE BOARD(updated)
              :- Bat/Bowl Option
              :- Bot bowls info
"""
from random import randint

#Defined Functions :-

def make_menu_square(str,z,l):
    a = len(str)+len(z)+len(l)
    print("*"*(a-7))
    print(str,z,l)
    print(" "*(a-7))
    print("*"*(a-7))

def toss(int):
    a = randint(1,10)
    b = int
    c = a + b   
    return c
#--------------------------User's Innings----------------------------------
def user_bats_first(i,n):
    global user_runs1
    global user_balls1
    user_runs1= 0
    user_balls1 = 0
    num_of_wickts = 0
    #print(user_name," will bat first")
    for i in range(i):
        while num_of_wickts < n:
            u = (input("hit's runs:- "))
            c = randint(1,10)
            
            if u == "Scoreboard":
                print("\nScore:-",user_runs1,"\tBalls:-",user_balls1,"\nWickets Fallen:-",num_of_wickts,"\tStrike Rate:-",(user_runs1/user_balls1)*100)
            
            elif int(u) == c:
                print("bot bowls:-",c)
                print("\nWICKET!")
                user_balls1 +=1
                num_of_wickts += 1
                print("\nWickets Fallen:- ",num_of_wickts)
                print("Runs after fall of",num_of_wickts,"wickets:- ",user_runs1)  
                
            elif int(u) != c:
                print("bot bowls:-",c)
                print(u,"runs in this ball")
                user_runs1 = user_runs1 + int(u)
                user_balls1 += 1
                break
            break
def user_bats_second(i,n):
    global user_runs2
    global user_balls2
    user_runs2 = 0
    user_balls2 = 0
    num_of_wickts = 0
 #   out = False
    for i in range(i):
        while num_of_wickts < n:
            while user_runs2 <= bot_runs1 :
                u = (input("hit's runs:- "))
                c = randint(1,10)
                
                if u == ("Scoreboard"):
                    print("\nScore:-",user_runs2,"\tBalls:-",user_balls2,"\nWickets Fallen:-",num_of_wickts,"\tRuns Remaining:-",bot_runs1 - user_runs2,"\nStrike Rate:-",(user_runs2/user_balls2)*100)
                
                elif int(u) == c:
                  #  out = True
                    print("bot bowls:-",c)
                    print("\nWICKET!")
                    user_balls2 += 1
                    num_of_wickts += 1
                    print("\nWickets Fallen:- ",num_of_wickts)
                    print("Runs after fall of",num_of_wickts,"wickets:- ",user_runs2)
                elif int(u) != c:
                    print("bot bowls:-",c)
                    print(u,"runs in this ball")
                    user_runs2 = user_runs2 + int(u)
                    user_balls2 += 1
                    break
                break
            break
#--------------------------Bots's Innings--------------------------------
def bot_bats_first(i,n):
    global bot_runs1
    global bot_balls1
    bot_runs1 = 0 
    bot_balls1 = 0
    bot_wickts = 0
    for i in range(i):
        while bot_wickts < n:
            c =randint(1,10)
            u = (input("bowl:- "))
            if u == ("Scoreboard"):
                print("\nScore:-",bot_runs1,"\tBalls:-",bot_balls1,"\nWickets Fallen:-",bot_wickts,"\tStrike Rate of Bots:-",(bot_runs1/bot_balls1)*100)
                
            elif int(u) != c:
                print("bot hits:-",c)
                print(c,"runs in this ball")
                bot_runs1 = bot_runs1 + c
                bot_balls1 += 1
                
            elif int(u) == c:
                print("bot hits:-",c)
                print("OUT!")
                bot_balls1 += 1
                bot_wickts += 1
                print("\nWickets Fallen:- ",bot_wickts)
                print("Runs after fall of",bot_wickts,"wickets:- ",bot_runs1)
                break
        
def bot_bats_second(i,n):
    global bot_runs2
    global bot_balls2
    bot_runs2 = 0 
    bot_balls2 = 0
    bot_wickts = 0
   # out = False
        
    for i in range(i):
        while bot_wickts < n:
            while bot_runs2 <= user_runs1 :
                c =randint(1,10)
                u = eval(input("bowl:- "))
                
                if u == ("Scoreboard"):
                    print("\nScore:-",bot_runs2,"\tBalls:-",bot_balls2,"\nWickets Fallen:-",bot_wickts,"\tRuns Remaining:-",user_runs1-bot_runs2,"\nStrike Rate of Bots:-",(bot_runs2/bot_balls2)*100)
                
                elif int(u) != c:
                    print("bot hits:-",c)
                    print(c,"runs in this ball")
                    bot_runs2 = bot_runs2 + c
                    bot_balls2 += 1
                    
                elif int(u) == c:
                    print("bot hits:-",c)
                   # out = True
                    print("OUT!")
                    bot_balls2 += 1
                    bot_wickts +=1
                    print("\nWickets Fallen:- ",bot_wickts)
                    print("Runs after fall of",bot_wickts,"wickets:- ",bot_runs2)
                    break
                break
            break
#------------------------------------------------------------------------------
# The Menu
user_name = input("Enter your team's name:- ")
user_wckts = int(input("Number of players in each team:- "))
intro = make_menu_square("Hi",user_name,"! Welcome to the ulimate cricket club. Hope you enjoy playing here.")
match_type = input("What would you like to play today?\nTest Match\nODI\nT20\n:-")
tm = "Test Match"
odi = "ODI"
t20 = "T20"
bat = "Batting"
bowl = "Bowling"
"""------------------------------------------------------------------------------"""

                           # Plays Test Match #

if match_type == tm:
    x = print("Nice choice. Since it is a testmatch, it will be of unlimited balls.\nYou better conserve your stamina and play smartly. ")
    print("Folks! Now its time to toss.")
    choose = input("Type E for even and O for Odd:")
    even = "E"
    odd = "O"
    bat_bowl = input("If you win the toss. What would you like to do first?\n->Batting\n->Bowling\nAns:- ")
    
    #Toss
    q = int(input("Enter a number: "))
    z = toss(q)
    test_toss = print("The sum of numbers chosen by",user_name,"and Team Bot is",z)
    
    
#In this case the user bats first :
    if choose == even:
        if z%2 == 0: #Condition of winning the toss
            if bat_bowl == "Batting":
                print(user_name,"won the toss and will Bat first.")
                user_bats_first(1000,user_wckts)
        
                print("\n",user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

                print("The second innings start.Team Bot comes in to Bat")
# Bot comes in to bat for 2nd inning   
                bot_bats_second(1000,user_wckts)
        
                print("\nTeam Bot has scored",bot_runs2,"in",bot_balls2,"balls")
                if user_runs1 > bot_runs2:
                    print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
                elif user_runs1 < bot_runs2:
                    print("BRAVO!Team Bot WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
                    
            elif bat_bowl == "Bowling":
                print(user_name,"won the toss and will Bowl first.")
                bot_bats_first(1000,user_wckts)
                print("\nTeam Bot has scored",bot_runs1,"of",bot_balls1,"balls")
                
                print("Target is of",bot_runs1)

                print("The second innings starts.",user_name,"comes in to Bat.")
    
# The user comes in to bat for 2nd inning
                user_bats_second(1000,user_wckts)
            
                print("\n",user_name,"has scored",user_runs2,"off",user_balls2,"balls")
    
                if user_runs2 > bot_runs1:
                    print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
                elif user_runs2 < bot_runs1:
                    print("BRAVO!Team Bot WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
 

#The bot bats in the first inning
        elif z%2 != 0: #Condition of losing the toss
            if bat_bowl == "Batting":
#Since I chose Batting but I lost the toss, I will Bowl
                print(user_name,"lost the toss and will Bowl first.")
                bot_bats_first(1000,user_wckts)
                print("\nTeam Bot has scored",bot_runs1,"of",bot_balls1,"balls")
                
                print("Target is of",bot_runs1)

                print("The second innings starts",user_name,"comes in to bat")
    
# The user comes in to bat for 2nd inning
                user_bats_second(1000,user_wckts)
            
                print("\n",user_name,"has scored",user_runs2,"off",user_balls2,"balls")
    
                if user_runs2 > bot_runs1:
                    print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
                elif user_runs2 < bot_runs1:
                    print("BRAVO!Team Bot WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
            
            elif bat_bowl == "Bowling":
#Since I chose bowling but I lost the toss, I will have to bat first
                print(user_name,"lost the toss and will bat first.")
                user_bats_first(1000,user_wckts)
        
                print("\n",user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

                print("The second innings start")
# Bot comes in to bat for 2nd inning   
                bot_bats_second(1000,user_wckts)
        
                print("\nTeam Bot has scored",bot_runs2,"in",bot_balls2,"balls")
                if user_runs1 > bot_runs2:
                    print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
                elif user_runs1 < bot_runs2:
                    print("BRAVO!Team Bot WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
 
# The user comes in to bat for 1st innings
    elif choose == odd:
        if z%2 != 0: #Condition of winning
            if bat_bowl == "Batting": 
                print(user_name,"won the toss and will Bat first.")
                user_bats_first(1000,user_wckts)
        
                print("\n",user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

                print("The second innings starts. Team Bot comes in to Bat.")
# Bot comes in to bat for 2nd inning   
                bot_bats_second(1000,user_wckts)
        
                print("\nTeam Bot has scored",bot_runs2,"in",bot_balls2,"balls")
                if user_runs1 > bot_runs2:
                    print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
                elif user_runs1 < bot_runs2:
                    print("BRAVO!Team Bot WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
                    
            elif bat_bowl == "Bowling":
                print(user_name,"won the toss and will Bowl first.")
                bot_bats_first(1000,user_wckts)
                print("\nTeam Bot has scored",bot_runs1,"off",bot_balls1,"balls")
                
                print("Target is of",bot_runs1)

                print("The second innings starts.",user_name,"comes in to bat.")
    
# The user comes in to bat for 2nd inning
                user_bats_second(1000,user_wckts)
            
                print("\n",user_name,"has scored",user_runs2,"off",user_balls2,"balls")
    
                if user_runs2 > bot_runs1:
                    print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
                elif user_runs2 < bot_runs1:
                    print("BRAVO!Team Bot WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
                
#The bot bats in the first inning
        elif z%2 == 0: #Condition of losing
            if bat_bowl == "Batting":
#Since I choose batting but lost the toss, I will bowl first
                print(user_name,"lost the toss and will Bowl first.")
                bot_bats_first(1000,user_wckts)
                print("\nTeam Bot has scored",bot_runs1,"off",bot_balls1,"balls")
                
                print("Target is of",bot_runs1)

                print("The second innings starts.",user_name,"comes in to bat.")
    
# The user comes in to bat for 2nd inning
                user_bats_second(1000,user_wckts)
            
                print("\n",user_name,"has scored",user_runs2,"off",user_balls2,"balls")
    
                if user_runs2 > bot_runs1:
                    print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
                elif user_runs2 < bot_runs1:
                    print("BRAVO!Team Bot WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
            elif bat_bowl == "Bowling":
#Since I chose Bowling and lost the toss, I will bat first.
                print(user_name,"lost the toss and will Bat first.")
                user_bats_first(1000,user_wckts)
        
                print("\n",user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

                print("The second innings starts. Team Bot comes in to Bat.")
# Bot comes in to bat for 2nd inning   
                bot_bats_second(1000,user_wckts)
        
                print("\nTeam Bot has scored",bot_runs2,"in",bot_balls2,"balls")
                if user_runs1 > bot_runs2:
                    print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
                elif user_runs1 < bot_runs2:
                    print("BRAVO!Team Bot WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
                    
                
                
#----------------------------------------------------------------------------#
               #                 Plays ODI
if match_type == odi:
    x = print("Nice choice. Since it is a ODI, it will be of 50 overs.\nYou better conserve your stamina and play smartly. ")
    print("Folks! Now its time to toss.")
    choose = input("Type E for even and O for Odd:")
    even = "E"
    odd = "O"
    bat_bowl = input("If you win the toss. What would you like to do first?\n->Batting\n->Bowling\nAns:- ")
    
    #Toss
    q = int(input("Enter a number: "))
    z = toss(q)
    test_toss = print("The sum of numbers chosen by",user_name,"and Team Bot is",z)
    
    
#In this case the user bats first :
    if choose == even:
        if z%2 == 0: #Condition of winning the toss
            if bat_bowl == "Batting":
                print(user_name,"won the toss and will Bat first.")
                user_bats_first(300,user_wckts)
        
                print("\n",user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

                print("The second innings start.Team Bot comes in to Bat")
# Bot comes in to bat for 2nd inning   
                bot_bats_second(300,user_wckts)
        
                print("\nTeam Bot has scored",bot_runs2,"in",bot_balls2,"balls")
                if user_runs1 > bot_runs2:
                    print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
                elif user_runs1 < bot_runs2:
                    print("BRAVO!Team Bot WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
                    
            elif bat_bowl == "Bowling":
                print(user_name,"won the toss and will Bowl first.")
                bot_bats_first(300,user_wckts)
                print("\nTeam Bot has scored",bot_runs1,"of",bot_balls1,"balls")
                
                print("Target is of",bot_runs1)

                print("The second innings starts.",user_name,"comes in to Bat.")
    
# The user comes in to bat for 2nd inning
                user_bats_second(300,user_wckts)
            
                print("\n",user_name,"has scored",user_runs2,"off",user_balls2,"balls")
    
                if user_runs2 > bot_runs1:
                    print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
                elif user_runs2 < bot_runs1:
                    print("BRAVO!Team Bot WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
 

#The bot bats in the first inning
        elif z%2 != 0: #Condition of losing the toss
            if bat_bowl == "Batting":
#Since I chose Batting but I lost the toss, I will Bowl
                print(user_name,"lost the toss and will Bowl first.")
                bot_bats_first(300,user_wckts)
                print("\nTeam Bot has scored",bot_runs1,"of",bot_balls1,"balls")
                
                print("Target is of",bot_runs1)

                print("The second innings starts",user_name,"comes in to bat")
    
# The user comes in to bat for 2nd inning
                user_bats_second(300,user_wckts)
            
                print("\n",user_name,"has scored",user_runs2,"off",user_balls2,"balls")
    
                if user_runs2 > bot_runs1:
                    print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
                elif user_runs2 < bot_runs1:
                    print("BRAVO!Team Bot WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
            
            elif bat_bowl == "Bowling":
#Since I chose bowling but I lost the toss, I will have to bat first
                print(user_name,"lost the toss and will bat first.")
                user_bats_first(300,user_wckts)
        
                print("\n",user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

                print("The second innings start")
# Bot comes in to bat for 2nd inning   
                bot_bats_second(300,user_wckts)
        
                print("\nTeam Bot has scored",bot_runs2,"in",bot_balls2,"balls")
                if user_runs1 > bot_runs2:
                    print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
                elif user_runs1 < bot_runs2:
                    print("BRAVO!Team Bot WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
 
# The user comes in to bat for 1st innings
    elif choose == odd:
        if z%2 != 0: #Condition of winning
            if bat_bowl == "Batting": 
                print(user_name,"won the toss and will Bat first.")
                user_bats_first(300,user_wckts)
        
                print("\n",user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

                print("The second innings starts. Team Bot comes in to Bat.")
# Bot comes in to bat for 2nd inning   
                bot_bats_second(300,user_wckts)
        
                print("\nTeam Bot has scored",bot_runs2,"in",bot_balls2,"balls")
                if user_runs1 > bot_runs2:
                    print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
                elif user_runs1 < bot_runs2:
                    print("BRAVO!Team Bot WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
                    
            elif bat_bowl == "Bowling":
                print(user_name,"won the toss and will Bowl first.")
                bot_bats_first(1000,user_wckts)
                print("\nTeam Bot has scored",bot_runs1,"off",bot_balls1,"balls")
                
                print("Target is of",bot_runs1)

                print("The second innings starts.",user_name,"comes in to bat.")
    
# The user comes in to bat for 2nd inning
                user_bats_second(300,user_wckts)
            
                print("\n",user_name,"has scored",user_runs2,"off",user_balls2,"balls")
    
                if user_runs2 > bot_runs1:
                    print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
                elif user_runs2 < bot_runs1:
                    print("BRAVO!Team Bot WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
                
#The bot bats in the first inning
        elif z%2 == 0: #Condition of losing
            if bat_bowl == "Batting":
#Since I choose batting but lost the toss, I will bowl first
                print(user_name,"lost the toss and will Bowl first.")
                bot_bats_first(300,user_wckts)
                print("\nTeam Bot has scored",bot_runs1,"off",bot_balls1,"balls")
                
                print("Target is of",bot_runs1)

                print("The second innings starts.",user_name,"comes in to bat.")
    
# The user comes in to bat for 2nd inning
                user_bats_second(300,user_wckts)
            
                print("\n",user_name,"has scored",user_runs2,"off",user_balls2,"balls")
    
                if user_runs2 > bot_runs1:
                    print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
                elif user_runs2 < bot_runs1:
                    print("BRAVO!Team Bot WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
            elif bat_bowl == "Bowling":
#Since I chose Bowling and lost the toss, I will bat first.
                print(user_name,"lost the toss and will Bat first.")
                user_bats_first(300,user_wckts)
        
                print("\n",user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

                print("The second innings starts. Team Bot comes in to Bat.")
# Bot comes in to bat for 2nd inning   
                bot_bats_second(300,user_wckts)
        
                print("\nTeam Bot has scored",bot_runs2,"in",bot_balls2,"balls")
                if user_runs1 > bot_runs2:
                    print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
                elif user_runs1 < bot_runs2:
                    print("BRAVO!Team Bot WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")

#------------------------------------------------------------------------------
#                   Plays T20
if match_type == t20:
    x = print("Nice choice. Since it is a T20, it will be of 20.\nYou better conserve your stamina and play smartly. ")
    print("Folks! Now its time to toss.")
    choose = input("Type E for even and O for Odd:")
    even = "E"
    odd = "O"
    bat_bowl = input("If you win the toss. What would you like to do first?\n->Batting\n->Bowling\nAns:- ")
    
    #Toss
    q = int(input("Enter a number: "))
    z = toss(q)
    test_toss = print("The sum of numbers chosen by",user_name,"and Team Bot is",z)
    
    
#In this case the user bats first :
    if choose == even:
        if z%2 == 0: #Condition of winning the toss
            if bat_bowl == "Batting":
                print(user_name,"won the toss and will Bat first.")
                user_bats_first(120,user_wckts)
        
                print("\n",user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

                print("The second innings start.Team Bot comes in to Bat")
# Bot comes in to bat for 2nd inning   
                bot_bats_second(120,user_wckts)
        
                print("\nTeam Bot has scored",bot_runs2,"in",bot_balls2,"balls")
                if user_runs1 > bot_runs2:
                    print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
                elif user_runs1 < bot_runs2:
                    print("BRAVO!Team Bot WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
                    
            elif bat_bowl == "Bowling":
                print(user_name,"won the toss and will Bowl first.")
                bot_bats_first(120,user_wckts)
                print("\nTeam Bot has scored",bot_runs1,"of",bot_balls1,"balls")
                
                print("Target is of",bot_runs1)

                print("The second innings starts.",user_name,"comes in to Bat.")
    
# The user comes in to bat for 2nd inning
                user_bats_second(120,user_wckts)
            
                print("\n",user_name,"has scored",user_runs2,"off",user_balls2,"balls")
    
                if user_runs2 > bot_runs1:
                    print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
                elif user_runs2 < bot_runs1:
                    print("BRAVO!Team Bot WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
 

#The bot bats in the first inning
        elif z%2 != 0: #Condition of losing the toss
            if bat_bowl == "Batting":
#Since I chose Batting but I lost the toss, I will Bowl
                print(user_name,"lost the toss and will Bowl first.")
                bot_bats_first(120,user_wckts)
                print("\nTeam Bot has scored",bot_runs1,"of",bot_balls1,"balls")
                
                print("Target is of",bot_runs1)

                print("The second innings starts",user_name,"comes in to bat")
    
# The user comes in to bat for 2nd inning
                user_bats_second(120,user_wckts)
            
                print("\n",user_name,"has scored",user_runs2,"off",user_balls2,"balls")
    
                if user_runs2 > bot_runs1:
                    print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
                elif user_runs2 < bot_runs1:
                    print("BRAVO!Team Bot WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
            
            elif bat_bowl == "Bowling":
#Since I chose bowling but I lost the toss, I will have to bat first
                print(user_name,"lost the toss and will bat first.")
                user_bats_first(120,user_wckts)
        
                print("\n",user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

                print("The second innings start")
# Bot comes in to bat for 2nd inning   
                bot_bats_second(120,user_wckts)
        
                print("\nTeam Bot has scored",bot_runs2,"in",bot_balls2,"balls")
                if user_runs1 > bot_runs2:
                    print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
                elif user_runs1 < bot_runs2:
                    print("BRAVO!Team Bot WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
 
# The user comes in to bat for 1st innings
    elif choose == odd:
        if z%2 != 0: #Condition of winning
            if bat_bowl == "Batting": 
                print(user_name,"won the toss and will Bat first.")
                user_bats_first(120,user_wckts)
        
                print("\n",user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

                print("The second innings starts. Team Bot comes in to Bat.")
# Bot comes in to bat for 2nd inning   
                bot_bats_second(120,user_wckts)
        
                print("\nTeam Bot has scored",bot_runs2,"in",bot_balls2,"balls")
                if user_runs1 > bot_runs2:
                    print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
                elif user_runs1 < bot_runs2:
                    print("BRAVO!Team Bot WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
                    
            elif bat_bowl == "Bowling":
                print(user_name,"won the toss and will Bowl first.")
                bot_bats_first(120,user_wckts)
                print("\nTeam Bot has scored",bot_runs1,"off",bot_balls1,"balls")
                
                print("Target is of",bot_runs1)

                print("The second innings starts.",user_name,"comes in to bat.")
    
# The user comes in to bat for 2nd inning
                user_bats_second(120,user_wckts)
            
                print("\n",user_name,"has scored",user_runs2,"off",user_balls2,"balls")
    
                if user_runs2 > bot_runs1:
                    print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
                elif user_runs2 < bot_runs1:
                    print("BRAVO!Team Bot WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
                
#The bot bats in the first inning
        elif z%2 == 0: #Condition of losing
            if bat_bowl == "Batting":
#Since I choose batting but lost the toss, I will bowl first
                print(user_name,"lost the toss and will Bowl first.")
                bot_bats_first(120,user_wckts)
                print("\nTeam Bot has scored",bot_runs1,"off",bot_balls1,"balls")
                
                print("Target is of",bot_runs1)

                print("The second innings starts.",user_name,"comes in to bat.")
    
# The user comes in to bat for 2nd inning
                user_bats_second(120,user_wckts)
            
                print("\n",user_name,"has scored",user_runs2,"off",user_balls2,"balls")
    
                if user_runs2 > bot_runs1:
                    print("BRAVO!",user_name,"WON BY",user_runs2 - bot_runs1,"RUNS AND LIFTS THE CUP")
    
                elif user_runs2 < bot_runs1:
                    print("BRAVO!Team Bot WON BY",bot_runs1 - user_runs2,"RUNS AND LIFTS THE CUP")
            elif bat_bowl == "Bowling":
#Since I chose Bowling and lost the toss, I will bat first.
                print(user_name,"lost the toss and will Bat first.")
                user_bats_first(120,user_wckts)
        
                print("\n",user_name, "has scored",user_runs1,"of",user_balls1,"balls \nThe target is of",user_runs1)

                print("The second innings starts. Team Bot comes in to Bat.")
# Bot comes in to bat for 2nd inning   
                bot_bats_second(120,user_wckts)
        
                print("\nTeam Bot has scored",bot_runs2,"in",bot_balls2,"balls")
                if user_runs1 > bot_runs2:
                    print("BRAVO!" ,user_name,"WON BY",user_runs1 - bot_runs2,"RUNS AND LIFTS THE CUP")
    
                elif user_runs1 < bot_runs2:
                    print("BRAVO!Team Bot WON BY",bot_runs2 - user_runs1,"RUNS AND LIFTS THE CUP")
                    