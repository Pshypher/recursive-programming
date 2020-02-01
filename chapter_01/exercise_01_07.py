# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 07:17:28 2019

@author: Pshypher
"""

# Decomposition: s(a) => a[0], s(a[1:n])
def sum_list_length_2(a):
    if a == []:
        return 0
    else:
        head = a[0]
        tail = a[1:]
        return (head + sum_list_length_2(tail))
    
# Some list
a = [5, -1, 3, 2, 4, -3]

# Function calls:
print(sum_list_length_2(a))        
        
    

    