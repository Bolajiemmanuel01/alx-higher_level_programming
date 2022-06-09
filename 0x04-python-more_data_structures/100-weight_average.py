#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    score_weight = 0
    total_weight = 0
    for tup in my_list:
        (score, weight) = tup
        score_weight += score * weight
        total_weight += weight
    return float(score_weight / total_weight) if total_weight > 0 else 0
