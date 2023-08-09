#!/usr/bin/python3

def remove_char_at(str, n):
    new_str = ""
    for index, value in enumerate(str):
        if index == n:
            continue
        new_str += value
    return new_str
