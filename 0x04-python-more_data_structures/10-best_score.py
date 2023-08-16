#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)

    best_score = 0
    max_key = None
    for key, i in a_dictionary.items():
        if best_score == 0 or i > best_score:
            best_score = i
            max_key = key
    return (max_key)
