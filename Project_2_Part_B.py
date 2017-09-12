#!/usr/bin/env Python

# Aingty Eung 
# 9/07/2017
# EE 381 Project 2
# Bernoulli Trials, Bayes' Rule, and General Probability
#   This program needs to be explained

import math

# The norm N is 10,000
N = 10000
# The adder A is 4,857
A = 4857
# The multiplier is 8,601
M = 8601

Can = [0, 0, 0]

# Input the Seed
#S = input("Enter seed number. ")
S = 0;

for i in range(2):
    S = (M*S + A)%N
    R = S/float(N) # Float division is used to obtain the number on (0,1) 
    Can_Number = math.floor(R*5 + 1)
    Can[i] = Can_Number
    print(Can)