#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.items())
    for item in sorted_dict:
        print(f"{item[0]}: {item[1]}")
