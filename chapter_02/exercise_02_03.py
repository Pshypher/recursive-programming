# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:52:47 2019

@author: Pshypher
"""

def sum_first_positive_int(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return (4 * sum_first_positive_int(n // 2) - 
                    n // 2)
    else:
        return (4 * sum_first_positive_int((n - 1) // 2) + 
                    (n + 1) // 2)

# Test
for n in range(1, 11):
    print(sum_first_positive_int(n), (n * (n + 1) // 2))        