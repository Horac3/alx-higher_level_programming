#!/usr/bin/python3
import sys

# Get the command-line arguments
arguments = sys.argv[1:]

# Initialize the variable to store the sum
total_sum = 0

# Iterate over the arguments
for arg in arguments:
    # Convert the argument to an integer and add it to the total sum
    total_sum += int(arg)

# Print the result of the addition
print(total_sum)
