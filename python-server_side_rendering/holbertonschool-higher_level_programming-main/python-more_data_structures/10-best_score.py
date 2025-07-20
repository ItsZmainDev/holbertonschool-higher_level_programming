#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    keys_list = list(a_dictionary.keys())
    i = 0
    best_key = None
    best_value = float('-inf')

    while i < len(keys_list):
        key = keys_list[i]
        if a_dictionary[key] > best_value:
            best_value = a_dictionary[key]
            best_key = key
        i += 1
    return best_key
