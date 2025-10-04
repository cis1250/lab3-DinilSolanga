#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
terms = int(input("How many terms of the fibonacci sequence would you like"))
# Validate that the input is a positive integer.
while (terms < 0):
  terms = int(input("Please enter a positive integer. "))
a, b = 0, 1
print("Fibonacci sequence:")    
# Use a for loop to print the Fibonacci sequence up to that many terms.
for i in range(n):
    print(a, end=" ")
    temp = a + b  
    a = b          
    b = temp  
