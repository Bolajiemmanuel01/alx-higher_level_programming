#!/usr/bin/python3
if __name__ == "__main__":
   import hidden_4
   all = dir(hidden_4)
   for string in all:
       if not string.startswith("__"):
           print("{:s}".format(string))
