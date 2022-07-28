#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Number Guessing

import random
n = random.randint(1, 99)
guess = int(input("Enter an integer from 1 to 99: "))
while n != ("guess"):
    print
    if guess < n:
        print("guess is low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print("guess is high")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print("you guessed it!")
        break
    print


# In[ ]:


## Dice roll generator

min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices:")
    print("The values are:")
    print(random.randint(min, max))
    print(random.randint(min, max))
    
    roll_again = raw_input("Roll the dices again?")


# In[ ]:


## temperature converter

temp_celsius =int(input("enter temp in celsius:"))
fahrenheit = (temp_celsius * 1.8) + 32
kelvin = (temp_celsius)+273.15
print(fahrenheit)
print(kelvin)


# In[ ]:


## Binary Search 


def binarySearch(array, x, low, high):

    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


# In[ ]:


## countdown

import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

countdown(10)


# In[ ]:


## measurement converter

kilometers = float(input("Enter value in kilometers: "))
conv_fac = 0.621371
miles = kilometers * conv_fac
meter = kilometers * 1000
centimeters = kilometers * 100000
print(miles,"miles")
print(meter,"meters")
print(centimeters,"cm")


# In[ ]:


## Rock Paper Scissors

import random

user_action=input("enter a choice(Rock,Paper,Scissors):")
possible_action=["Rock","Paper","Scissors"]
computer_action=random.choice(possible_action)
print(f"/nYou chose:{user_action},computer chose:{computer_action}./n")

if user_action == computer_action:
    print(f"both players selected(user_action) it is Tie!")
elif user_action == "Rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win")
    else:
        print("Paper cover Rocks! You loose:")
elif user_action == "Paper":
    if computer_action == "Rock":
        print("Paper cover Rocks! You win")
    else:
        print("Scissor cut Papers! You loose")
elif user_action == "Scissors":
    if computer_action == "Paper":
        print("Scissor cut Papers! You win")
    else:
        print("Rock smashes scissors! You loose")
   

