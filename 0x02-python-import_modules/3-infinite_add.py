#!/usr/bin/python3
 if __name__ == "__main__":
    from sys import argv
    a = len(argv)
    b = 0
    if a == 1:
        print("0")
    else:
        for i in range(1, a):
            b += int(argv[i])
        print("{}".format(b))
