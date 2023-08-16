#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = []
    unique_add = 0
    for x in my_list:
        if x not in result:
            result.append(x)
            unique_add += x
    return (unique_add)
