def safe_print_list(my_list=[], x=0):
    count = 0
    for idx in range(x):
        try:
            print(f"{my_list[idx]}", end="")
            count += 1
        except IndexError:
            break
    print()
    return count
