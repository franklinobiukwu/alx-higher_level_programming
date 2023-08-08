#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

mod = 10

if number < 0:
    mod *= -1

last_digit = number % mod

if last_digit == 0:
    str = "is 0"
elif last_digit < 6 and last_digit != 0:
    str = "is less than 6 and not 0"
elif last_digit > 5:
    str = "is greater than 5"

print(f"Last digit of {number} is {last_digit} and {str}")
