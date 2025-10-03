#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
num_1 = 0
num_2 = 1
terms = int(input("How many terms of the Fibonacci sequence would you like to see?: "))
if terms <= 0:
  print("Please enter a positive integer.")
else:  
  print("The Fibonacci sequence is: ", end="")
  for i in range(terms + 1):
    print(num_1, end=" ")
    num_1, num_2 = num_2, num_1 + num_2


