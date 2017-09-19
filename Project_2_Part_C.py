#!/usr/bin/env Python

# Aingty Eung 
# 9/17/2017
# EE 381 Project 2
# This Program evaluates Bayes Rule Probabilities.

a = float(input("Enter the Probability of the pathology: "))
b = float(input("Enter the accuracy of the diagnostic: "))
c = float(input("Enter the probability of a false positive: "))

p = (a*b)/((a*b)+((1-a)*c))

print 'The probability of actually having the pathology is = ',p