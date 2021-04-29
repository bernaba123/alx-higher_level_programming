#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = len(sys.argv)
    if s == 1:
        print("{:d} arguments.".format(s - 1))
    elif s == 2:
        print("{:d} argument:".format(s - 1))
        print("{:d}: {:s}".format(len(s, sys.argv[1]))
    else:
        print("{:d} arguments:".format(s - 1))
        for i in range(s - 1):
            print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
