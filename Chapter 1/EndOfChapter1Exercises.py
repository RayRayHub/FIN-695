# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:44:58 2023

@author: szcze
"""

# 1
print("Output for question 1.")
print(2) # '2'
print(3**2) # 9
print(7//3) # 2
print(7/3) # 2.3333
print(7%3) # 1
print(2+2) # 4
print(10*2) # 20
print()

#2
print("Output for question 2.")
Name1 = 'Kentucky '
Name2 = "Wildcats"
#What is the output from each of the following lines of command? Verify your answers in Spyder.
print(type(Name1)) # str
print(type(Name2)) # str
print(Name1+Name2) # Kentucky Wildcats
print(Name2+Name1) # WildcatsKentucky 
print(Name2+' @ '+Name1) # Wildcats @ Kentucky
print(3* Name2) # WildcatsWildcatsWildcats
print()

#3
print("Output for question 3.")
x=3.458 
y=-2.35
# what is the result for each of the following?
print(type(x)) # float
print(type(y)) # float
print(round(x,2)) # 3.46
print(round(y,1)) # -2.4
print(round(x,0)) # 3.0
print()

#4
print("Output for question 4.")
a=57
b=-3
c=0
# What is the outcome from each of the following?
print(type(b)) # int
print(str(a)) # '57'
print(float(c)) # 0.0
print()

#5
print("Output for question 5.")
print(type(5==9)) # bool
print('8<7') # '8<7'
print(5==9) # False
print(type('5==9')) # str
print(type('8<7')) # str
print(type('True')) # str
print()

#6
print("Output for question 6.")
print(int(-23.0)) # -23
print(int("56")) # 56
print(int(-2.35)) # -2
print(str(-23.0)) # '-23.0'
print(float(8)) # 8.0
print()

#7
print("Output for question 7.")
print(int(True)) # 1
print(float(False)) # 0.0
print(str(False)) # 'False'
print()

#8
print("Output for question 8.")
print(bool(0)) # False
print(bool(-23)) # True
print(bool(17.6)) # True
print(bool('Python')) # True
print()

#9
print("Output for question 9.")
print("global # no reserved keyword in python.")
print("2print # no starts with a number instead of letter or underscore.")
print("print2 # yes")
print("_squ # yes")
print("list # no built in function")
print()

#10
print("Output for question 10.")
for letter in ("A", "B", "C"):
    if letter == "B":
        break
    for num in (1, 2):
        print(f"this is {letter}{num}") # A1 A2 
print()
        
#11
print("Output for question 11.")
for letter in ("A", "B", "C"):
    if letter == "B":
        continue
    for num in (1, 2):
        print(f"this is {letter}{num}") # A1 A1 C1 C2
print()
        
#12
print("Output for question 12.")
for letter in ("A", "B", "C"):
    if letter == "B":
        pass
    for num in (1, 2):
        print(f"this is {letter}{num}") # all
print()
        
#13
print("Output for question 13.")
for letter in ("A","B"):
    for num in (1,2):
        print(f"this is {letter}{num}") # A1 A2 B1 B2