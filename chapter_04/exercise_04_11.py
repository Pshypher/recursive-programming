# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:03:49 2019

@author: Pshypher
"""

def num_processed_bit(y):
    
    def decimal_to_binary(v):
        if v < 2:
            return v
        else:
            return (decimal_to_binary(v // 2)
                    * 10 + (v % 2))
    
    def least_significant_bit(x):
        if x == 0:
            return 0
        elif x == 1 or (x % 10) == 1:
            return 1
        else:
            return least_significant_bit(x // 10) + 1
        

    if y == 1:
        return 1
    else:
        binary = decimal_to_binary(y)
        bits = least_significant_bit(binary)
        return (num_processed_bit(y - 1)
                + bits)
        
# Test
for i in range(1, 5 + 1):
    limit = 2 ** i - 1
    print("number of processed bits", 
          num_processed_bit(limit))        
        