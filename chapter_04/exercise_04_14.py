# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:28:59 2019

@author: Pshypher
"""

def pascal(n):
    
    def row_subset(a):
        if len(a) < 2:
            return []
        else:
            x = a[0] + a[1]
            return [x] + row_subset(a[1:])
    
    if n == 0:
        return [1]
    else:
        row = [1]
        previous_row = pascal(n - 1)
        row.extend(row_subset(previous_row))
        row.append(1)
    return row

# Test
for n in range(0, 6):
    print(pascal(n))