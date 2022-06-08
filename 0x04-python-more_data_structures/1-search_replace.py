#!/usr/bin/python3
from copy import copy


def search_replace(my_list, search, replace):
    copy_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            copy_list.append(replace)
        else:
            copy_list.append(my_list[i])
        return copy_list
    