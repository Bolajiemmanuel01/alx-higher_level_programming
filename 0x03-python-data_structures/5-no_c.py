#!/usr/bin/python3
def no_c(my_string):
    for letters in my_string:
        if letters in 'cC':
            print('', end="")
        else:
            print(letters, end="")
