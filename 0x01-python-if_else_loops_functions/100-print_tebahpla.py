#!/usr/bin/python3

count = 0

for i in reversed(range(ord('a'), ord('z') + 1)):
    count += 1
    if (count % 2 == 0):
        num = -32
    else:
        num = 0
    print("{}".format(chr(i + num)), end="")
