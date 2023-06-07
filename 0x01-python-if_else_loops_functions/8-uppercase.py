#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        result += chr(ord(c) & 0b11011111)  # Flip the 6th bit to convert to uppercase
    print(result)