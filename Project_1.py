#!/usr/bin/env Python

# Aingty Eung 
# 8/31/2017
# EE 381 Project 1
# Pseudorandom Number Generator
#   This program will generate a number based on user's input range.

import time

# The norm N is 10,000
N = 10000

# The adder A is 4,857
A = 4857

# The multiplier is 8,601
M = 8601

S = input("Enter seed number. ")
#timeSeed = time.time()

for i in range(100):
    S = (M*S + A)%N
    R = S/float(N) # Float division is used to obtain the number on (0,1)
    print(format(R, '.4f')) # Print number to 4 decimal places
