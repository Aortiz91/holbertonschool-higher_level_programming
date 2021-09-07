#!/usr/bin/python3
for i in range(97, 123):
    try:
        i == 101
    except:
        continue
    try:
        i == 113
    except:
        continue
    print("{}".format(chr(i)), end="")
