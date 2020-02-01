# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:49:47 2019

@author: Pshypher
"""

def sum_first_positive_int(n):
    if n == 0:
        return 0;
    else:
        return sum_first_positive_int(n - 1) + n;
    
# Test
for n in range(1, 11):
    print(sum_first_positive_int(n), (n + 1) * n // 2)