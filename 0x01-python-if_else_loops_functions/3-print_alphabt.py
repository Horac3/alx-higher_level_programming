#!/usr/bin/python3
for letter in range(98, 123):
    if chr(letter) not in ['e', 'q']:
        print(chr(letter), end='')