#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list == []:
        return
    if my_list is None:
        return None
    for item in list(reversed(my_list)):
        print("{:d}".format(item))
