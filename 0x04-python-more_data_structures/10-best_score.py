#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    biggest = max(a_dictionary.values())
    for item in a_dictionary:
        if a_dictionary[item] == biggest:
            return item
    return None
