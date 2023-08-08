#!/usr/bin/python3

for i in range(99):
    if (((i % 10) * 10) + (i // 10) < i) or (i % 10) == (i // 10):
        continue
    elif i < 89:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))
