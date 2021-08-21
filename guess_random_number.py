# -*- coding: utf-8 -*-
"""Guess_Random_Number.ipynb"""


import math
import random

low = int(input("Enter the lower range:"))
high = int(input("Enter the higher range:"))

x = random.randint(low,high)
times = round(math.log(high-low+1,2))
print("\n\tYou have only ",times,"chances to guess the integer!\n")

count = 0
while count < times:
  count += 1
  guess = int(input("Guess the number:"))
  if (x == guess):
    print("\n\tCongratulations! You did it on ", count," try!")
    break
  elif(x > guess):
    print("You guessed too small!")
  else:
    print("You guessed too large!")

if(count >= times):
  print("\n\tThe number is:",x)
  print("\tBetter luck next time!")
