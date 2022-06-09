#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    score_weight = 0
    total_weight = 0
    for tup in my_list:
        score_weight += tup[0] * tup[1]
        total_weight += tup[1]
    return float(score_weight / total_weight)
