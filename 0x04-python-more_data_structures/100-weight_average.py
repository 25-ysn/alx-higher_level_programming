#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    number = 0
    val = 0
    for x in my_list:
        number += x[0] * x[1]
        val += x[1]
    return (number / val)
