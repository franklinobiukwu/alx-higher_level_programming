#!/usr/bin/python3

def common_elements(set_1, set_2):
    common = []
    for i in set_1:
        if i not in set_2:
            continue
        else:
            common.append(i)
    return set(common)
