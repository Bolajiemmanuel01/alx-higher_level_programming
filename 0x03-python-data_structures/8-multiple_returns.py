#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = ()
    a = len(sentence)
    b = sentence[0]
    if a == 0:
        my_tuple = 0, "None"
        return my_tuple
    else:
        my_tuple = a, b
        return my_tuple
