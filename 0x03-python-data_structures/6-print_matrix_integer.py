#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            if (y == x):
                print("{:d}".format(y))
            else:
                print("{:d} ".format(y), end='')
        print("")
