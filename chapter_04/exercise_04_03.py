# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 18:21:45 2019

@author: Pshypher
"""
import numpy as np

def power_square_matrix(a, n):
    if n == 0:
        return np.identity(a.shape[0])
    else:
        sub_a = power_square_matrix(a, n - 1)
        return np.dot(sub_a, a)        


# Test
x = np.array([[1, 1], [1, 0]], np.int32)

for i in range(1, 10 + 1):
    a = power_square_matrix(x, i)
    print(a[0, 1])       
        