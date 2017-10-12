#!/usr/bin/env Python

# Aingty Eung 013462772 10/12/17
## Exam 1 Code: Dice Roll


import random

z = [0] * 11


print "\nPossible Values for Z = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}\n"
print "\tExpected Probability:\n\tZ(2) = 1/36\n\tZ(3) = 2/36\n\tZ(4) = 3/36\n\tZ(5) = 4/36\n\tZ(6) = 5/36\n\tZ(7) = 6/36\n\tZ(8) = 5/36\n\tZ(9) = 4/36\n\tZ(10) = 3/36\n\tZ(11) = 2/36\n\tZ(12) = 1/36\n"

for i in range(10000):
    X = random.randint(1,6)
    Y = random.randint(1,6)
    Z = X + Y

    if (Z == 2):
        z[0] += 1
    if (Z == 3):
        z[1] += 1
    if (Z == 4):
        z[2] += 1
    if (Z == 5):
        z[3] += 1
    if (Z == 6):
        z[4] += 1
    if (Z == 7):
        z[5] += 1
    if (Z == 8):
        z[6] += 1
    if (Z == 9):
        z[7] += 1
    if (Z == 10):
        z[8] += 1
    if (Z == 11):
        z[9] += 1
    if (Z == 12):
        z[10] += 1

print "Actual Result:"
print "Z(2) = %.0f/10000 = %.2f " %(z[0], (z[0]/float(10000))*100) 
print "Z(3) = %.0f/10000 = %.2f " %(z[1], (z[1]/float(10000))*100)
print "Z(4) = %.0f/10000 = %.2f " %(z[2], (z[2]/float(10000))*100)
print "Z(5) = %.0f/10000 = %.2f " %(z[3], (z[3]/float(10000))*100)
print "Z(6) = %.0f/10000 = %.2f " %(z[4], (z[4]/float(10000))*100)
print "Z(7) = %.0f/10000 = %.2f " %(z[5], (z[5]/float(10000))*100)
print "Z(8) = %.0f/10000 = %.2f " %(z[6], (z[6]/float(10000))*100)
print "Z(9) = %.0f/10000 = %.2f " %(z[7], (z[7]/float(10000))*100)
print "Z(10) = %.0f/10000 = %.2f " %(z[8], (z[8]/float(10000))*100)
print "Z(11) = %.0f/10000 = %.2f " %(z[9], (z[9]/float(10000))*100)
print "Z(12) = %.0f/10000 = %.2f " %(z[10], (z[10]/float(10000))*100)


