#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    izzoh = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            izzoh[count] = True
        else:
            izzoh[count] = False
    return(izzoh)

