#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(repr (number)[-1])
if (number < 0):
    last_digit = -last_digit
if (last_digit < 6):
    if (last_digit == 0):
        print(f"Last digit of {number} is {last_digit} and is 0")
    else:
        print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
if (last_digit > 5):
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
