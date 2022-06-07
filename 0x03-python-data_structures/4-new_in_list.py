#!/usr/bin/python3
def new_in_list(my_list, idx, my_element):

    if idx < 0:
        print(my_list)

    length = len(my_list)

    if idx < length:
        my_list[idx] = my_element
        
        return (my_list)
