#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    izzoh_list = my_list[:]
    if 0 <= idx < len(my_list):
        izzoh_list[idx] = element
        return(izzoh_list)
    return(my_list)
