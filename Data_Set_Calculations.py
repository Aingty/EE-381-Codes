#!/usr/bin/env Python

# Basic Statistics
# We'll determine the mean and median of a data set.

counter = int(input("\nEnter the number of elements in the list: "))
data_Set = [0]*counter
for k in range(counter):
    element = int(input("Enter a data: "))
    data_Set[k] = element


# Here is a data set
#data_Set = [3, 6, 1, 9, 3, 6]
print("Here is your list: %s" %data_Set)

# How do we determine the mean?
print("\nThe following are your data:")

# We're going to use two function sum and len.
s = sum(data_Set)
print("Sum: %s" %s)

l = len(data_Set)
print("Length: %s" %l)

mean = s/float(l)
print("Mean: %s" %mean)

# Hey!, Everybody! Let's determine the median of the data set.

new_Data_Set = sorted(data_Set)
print("Data Set Sorted: %s" %new_Data_Set)

if l % 2 == 0:
    n1 = l/2
    n2 = (l/2) + 1
    
    # CAREFUL!! These are float numbers. So cast them to Int
    n1 = int(n1) - 1
    n2 = int(n2) - 1
    
    # The median in this case would be as follows.
    median = (new_Data_Set[n1] + new_Data_Set[n2])/2
else:
    n = (l + 1)/2
    n = int(n) - 1
    
    # The median in this case would be as follows.
    median = new_Data_Set[n]

print("Median: %s\n" %median)

