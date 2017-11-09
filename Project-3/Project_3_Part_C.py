#!/usr/bin/env Python

# Aingty Eung 
# 10/10/2017
# EE 381 Project 3_Part_C
# Binomial Distribution
## If the problem is a binomially distributed Random Variable...
### Let n be the number of trials be 5 with probablility of success
### Let p be equal to 0.7

import random
# Below is a frequncy simulation program.
n = int(input("Enter the number of trails: ")) # Number of trials
p = float(input("Enter the probability of successes: ")) # The probability of success
x_low = int(input("Enter the lowest number of successes: ")) # Number of successes
x_high = int(input("Enter the highest number of successes: "))
j = 0 # Counter
N = 50000 # The number of requency repetitions
s = 0

trial = [0] # List to record trial
trial = trial * n # Set the size of the trial list

for k in range(N):
    for i in range(n):
        r = random.uniform(0,1)
        
        if r < p:
            trial[i] = 1
        else:
            trial[i] = 0
        
        s = sum(trial)

    if (s >= x_low) and (s <= x_high):
        j += 1

prob = j / float(N)
print(prob)    
