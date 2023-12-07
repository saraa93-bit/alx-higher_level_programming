#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set(my_list)  # Convert the list to a set to remove duplicates
    result = sum(unique_set)   # Sum all unique integers in the set
    return result
