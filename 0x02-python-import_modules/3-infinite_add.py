#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = 0
    for t in range(len(sys.argv) - 1):
        s += int(sys.argv[t + 1])
    print(s)
