#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    arraynames = dir(hidden_4)
    for i in range(0, len(arraynames)):
        if arraynames[i][0:2] != "__":
            print("{}".format(arraynames[i]))
