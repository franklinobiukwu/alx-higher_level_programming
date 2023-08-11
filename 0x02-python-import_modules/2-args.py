#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv


    if len(argv) == 1:
        title = "argument."
    elif len(argv) > 2:
        title = "arguments:"
    else:
        title = "argument:"

    print("{:d} {}".format(len(argv) - 1, title))

    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))
