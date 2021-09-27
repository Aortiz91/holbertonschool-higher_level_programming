#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            n = int(my_list[i])
            print("{:d}".format(n), end="")
            counter += 1
        except (TypeError, ValueError):
            pass
    print()
    return counter
