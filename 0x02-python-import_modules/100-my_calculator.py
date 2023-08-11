#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    if argv[2] not in ("+", "-", "*", "/"):
        print(f"Uknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == "+":
        print(f"{a} {argv[2]} {b} = {add(a, b):}")
    elif argv[2] == "-":
        print(f"{a} {argv[2]} {b} = {sub(a, b):}")
    elif argv[2] == "*":
        print(f"{a} {argv[2]} {b} = {mul(a, b):}")
    elif argv[2] == "/":
        print(f"{a} {argv[2]} {b} = {div(a, b):}")
