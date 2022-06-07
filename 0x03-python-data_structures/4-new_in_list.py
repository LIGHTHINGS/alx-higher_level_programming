#!/usr/bin/python3
def new_in_list(my_list, idx, my_element):

    length = len(my_list)
    new_list = my_list[:]

    if idx < 0:
        return (my_list)

    elif idx < length:
        new_list[idx] = my_element
        
        return (new_list)
