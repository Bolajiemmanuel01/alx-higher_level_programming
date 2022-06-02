#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    Total = 0
    for i in range(1, len(sys.argv)):
        Total += int(sys.argv[i])
    print("{}".format(Total))
