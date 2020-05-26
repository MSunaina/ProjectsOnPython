# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 15:34:42 2020

@author: user
"""
print("Welcome To The FizzBuzz Game")
n=int(input("Please Enter The Range To Play:-" ))
for i in range(n):
    if i%3==0 and i%5==0: # Multiples of three and five
        print(i,"->FIZZBUZZ")
    elif i%3==0:          #Multiples of three
        print(i,"->FIZZ")
    elif i%5==0:          #Multiples of five
        print(i,"->BUZZ")
    else:
        print(i)