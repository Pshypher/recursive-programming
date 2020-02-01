# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 13:56:28 2020

@author: Pshypher
"""

def position_element_search(a, lower, upper):
    if lower > upper:    # empty list
        return -1
    else:
        if a[lower] == lower:
            return lower
        elif a[upper] == upper:
            return upper
        else:
            return position_element_search(a, lower + 1, upper - 1)

def position_element_search_wrapper(a):
    return position_element_search(a, 0, len(a) - 1)
        
# Test
print(position_element_search_wrapper([]))
print(position_element_search_wrapper([0]))
print(position_element_search_wrapper([2]))
print(position_element_search_wrapper([3, 2]))
print(position_element_search_wrapper([2, 5, 6]))
print(position_element_search_wrapper([1, 0, 2, 4]))
print(position_element_search_wrapper([6, 5, 5, 3, 6]))
print(position_element_search_wrapper([1, 9, 7, 0, 3, 7, 6]))
print(position_element_search_wrapper([-3, -1, 2, 5, 6, 7, 9]))
print(position_element_search_wrapper([3, 1, 4, 1, 5, 9, 2, 6]))
