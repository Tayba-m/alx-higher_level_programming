#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    c = len(sys.argv) - 1
    if c == 0:
        print("0 arguments.")
    elif c == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(c))
    for t in range(c):
        print("{}: {}".format(t + 1, sys.argv[t + 1]))
