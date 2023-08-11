#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        print(len(argv))
        exit(1)
    if argv[2] not in ("+", "-", "*", "/"):
        print(f"Uknown operator. Available operators: +, -, * and /")
        print(argv[2])
        print(type(argv[2]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == "+":
        print(f"{a:d} {argv[2]} {b:d} = {add(a, b):d}")
    elif argv[2] == "-":
        print(f"{a:d} {argv[2]} {b:d} = {sub(a, b):d}")
    elif argv[2] == "*":
        print(f"{a:d} {argv[2]} {b:d} = {mul(a, b):d}")
    elif argv[2] == "/":
        print(f"{a:d} {argv[2]} {b:d} = {div(a, b):d}")
