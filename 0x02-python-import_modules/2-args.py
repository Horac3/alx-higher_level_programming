#!/usr/bin/python3
import sys

# Get the command-line arguments
arguments = sys.argv[1:]

# Print the number of arguments
num_arguments = len(arguments)
print("Number of argument(s):", num_arguments)

# Print the list of arguments or a dot if no arguments were passed
if num_arguments > 0:
    print("Arguments:")
    for i, arg in enumerate(arguments, start=1):
        print("{}: {}".format(i, arg))
else:
    print(".")
