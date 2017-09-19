#!/usr/bin/env Python

# Aingty Eung 
# 9/14/2017
# EE 381 Project 2
# Bernoulli Trials, Bayes' Rule, and General Probability


import math

# The norm N is 10,000
N = 100000
# The adder A is 4,857
A = 4857
# The multiplier is 8,601
M = 8601

Ball = [0, 0, 0]

# Initialize the counters
sum_One = 0
sum_Two = 0

# Initialize the Seed
#S = input("Enter seed number. ")
S = 0

# Initialize the number of Experiments
k = int(input('Enter the number of experiments. '))

for k in range(k): 
    for i in range(3):
        S = (M*S + A)%N
        R = S/float(N) # Float division is used to obtain the number on (0,1) 

        # Generating number 1 - 5
        Ball_Number = math.floor(R*5 + 1)

        # Saving the randomized number into list
        Ball[i] = int(Ball_Number)

        if (i == 2) & ((Ball[0] != Ball[1]) & (Ball[1] != Ball[2]) & (Ball[0] != Ball[2])):
            sum_One += 1
            #print('Distinct', Ball)
        elif i == 2:
            sum_Two += 1
            #print('Not Distinct', Ball)

print(sum_One / float((sum_One + sum_Two)))