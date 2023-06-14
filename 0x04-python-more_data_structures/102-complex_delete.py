#!/usr/bin/python3
def complex_delete(my_dict, value):
    izzoh = my_dict.copy()
    for j, v in izzoh.items():
        if value == v:
            my_dict.pop(k)
    return my_dict
