#!/usr/bin/env python3

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
# you have 2 issues with your code, 1 is looping over 'n' on line 11, you should be looping over "terms". The second is that your code breaks when a string or 0 is entered. -2
