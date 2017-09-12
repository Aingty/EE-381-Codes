#!/usr/bin/env Python

# Aingty Eung 
# 9/07/2017
# EE 381 Project 2
# Bernoulli Trials, Bayes' Rule, and General Probability
#   This program needs to be explained

print('Bernoulli Trial Simulation.')

# Cast the number to float for success rate
p = float(input('Enter the Probability of Success:  '))

k = int(input('Enter the number of trails:  '))

# Using the old random number generator code from Project 1
# The norm N is 10,000
N = 10000
# The adder A is 4,857
A = 4857
# The multiplier is 8,601
M = 8601

# Input the Seed
#S = input("Enter seed number. ")
S = 1;

for i in range(k):
    S = (M*S + A)%N
    R = S/float(N) # Float division is used to obtain the number on (0,1) 
    print(format(R, '.4f')) # Print number to 4 decimal places
# End of Project 1 random number generator
    if R < p:
        print('Success!\n')
    else:
        print('Failure!\n')
