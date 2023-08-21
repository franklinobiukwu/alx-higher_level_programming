#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    digit = 0
    prev_value = 0

    for letter in roman_string:
        value = roman[letter]

        if value > prev_value:
            digit += value - 2 * prev_value
        else:
            digit += value

        prev_value = value

    return digit
