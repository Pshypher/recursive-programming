# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:04:25 2019

@author: Pshypher
"""

def max_list_length(a):
    if (len(a) == 1):
        return a[0]
    else:
        m = max_list_length(a[0:len(a) - 1])
        return max(m, a[len(a) - 1])
    
# Some list
v = [5, -1, 3, 2, 4, 7, 2]

# Function call
print(max_list_length(v))