# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 07:51:40 2020

@author: Pshypher
"""

def maximum_sublist_indices(a, lower, upper):
    middle = (lower + upper) // 2
    
    if lower == upper:
        return (lower, upper)
    else:
        lower_a, upper_a = maximum_sublist_indices(a, lower, middle)
        lower_c, upper_c = maximum_sublist_indices(a, middle + 1, upper)
        lower_b, upper_b = upper_a + 1, lower_c - 1 
        
        sum_abc = sum(a[lower_a : upper_c + 1])
        sum_ab = sum(a[lower_a : upper_b + 1])
        sum_bc = sum(a[lower_b : upper_c + 1])
        sum_a = sum(a[lower_a : upper_a + 1])
        sum_c = sum(a[lower_c : upper_c + 1])
        
        m = max(sum_abc, sum_ab, sum_bc, sum_a, sum_c)
        
        if m == sum_abc:
            return (lower_a, upper_c)
        elif m == sum_ab:
            return (lower_a, upper_b)
        elif m == sum_bc:
            return (lower_b, upper_c)
        elif m == sum_a:
            return (lower_a, upper_a)
        else:
            return (lower_c, upper_c)

def maximum_sublist(a):
    lower, upper = maximum_sublist_indices(a, 0, len(a) - 1)
    return a[lower : upper + 1]    
        
        
# Test
a = [-6, 3, -2, -5, 2, 3, -5]
print(maximum_sublist(a))
print(sum(maximum_sublist(a)))
print() 

a = [-1, -4, 5, 2, -3, 4, 2, -5] 
print(maximum_sublist(a))
print(sum(maximum_sublist(a)))     