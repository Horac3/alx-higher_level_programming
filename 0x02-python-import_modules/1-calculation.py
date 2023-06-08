#!/usr/bin/python3

"""Print the sum, difference, multiple and quotient of 10 and 5."""
from calculator_1.py import add, sub, mul, div

"""Define the variables"""
a = 10
b = 5

"""Call the functions and print the result"""
print("{}+{}={}".format(a, b, add(a, b)))
print("{}-{}={}".format(a, b, sub(a, b)))
print("{}*{}={}".format(a, b, mul(a, b)))
print("{}/{}={}".format(a, b, div(a, b)))
