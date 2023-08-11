#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)

    operations = {"+": add, "-": sub, "*": mul, "/": div}

    if argv[2] not in list(operations.keys()):
        print(f"Uknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    #print(f"{a} {argv[2]} {b} = {operations[argv[2]](a, b)}")
    print("{} {} {} = {}".format(a, argv[2], b, operations[argv[2]](a, b)))
