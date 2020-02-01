# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 05:41:55 2020

@author: Pshypher
"""

def largest_even_index(a, i, lower, upper):
    if lower > upper:
        if a == [] or a[i] % 2:
            return -1
        else:
            return i
    else:
        middle = (lower + upper) // 2
        if a[middle] % 2:
            return largest_even_index(a, i, lower, middle - 1)
        else:
            return largest_even_index(a, middle, middle + 1, upper)
        
def largest_even_index_wrapper(a):
    middle = (0 + len(a)) // 2
    return largest_even_index(a, middle, 0, len(a) - 1)        
        
# Test
print(largest_even_index_wrapper([]))
print(largest_even_index_wrapper([0]))
print(largest_even_index_wrapper([1]))
print(largest_even_index_wrapper([4, 0, -2]))
print(largest_even_index_wrapper([3, -5, 1]))
print(largest_even_index_wrapper([-2, 4, 0, 7]))
print(largest_even_index_wrapper([17, 13, 3, -31, 29, -7]))
print(largest_even_index_wrapper([8, 2, 12, -10, 3, 11, 17]))
print(largest_even_index_wrapper([2, -4, 10, 8, 0, 12, 9, 3, -15, 3, 1]))            