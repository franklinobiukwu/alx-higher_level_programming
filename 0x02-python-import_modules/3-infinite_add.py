#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    sum = int(argv[1])
    for i in range(2, len(argv)):
        sum += int(argv[i])
    print(sum)
