#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if my_list[i] != int:
                print("{:d}".format(x))
        except (typeError, ValueError):
            continue
