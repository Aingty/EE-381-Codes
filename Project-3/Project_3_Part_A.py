#!/usr/bin/env Python

# Aingty Eung 
# 10/10/2017
# EE 381 Project 3_Part_A
# Binomial Distribution
## If the problem is a binomially distributed Random Variable...
### Let n be the number of trials be 5 with probablility of success
### Let p be equal to 0.7

# Below is a frequncy simulation program.
n = 5
p = 0.7
x = 3
j = 0 # Counter

N = 5000000 # The number of requency repetitions

trial = [0] # List to record trial
trial = trial * n # Set the size of the trial list

for k in range(N):
    print "\n"
    for i in range(n):
        r = random.uniform(0,1)
        
        if r < p:
            trial[i] = 1
        else:
            trial[i] = 0
        
        s = sum(trial)
        print "%s : Sum = %d" %(trial, s)
    print "\n"

    if s == x:
        j += 1

prob = j / float(N)
print(prob)    
