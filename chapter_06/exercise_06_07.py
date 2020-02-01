# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:58:29 2020

@author: Pshypher

Computes the multplication of two matrices via recursion using the 
decomposition given by 
    AB = [A1 | A2].[B1]
                   ----  =  [A1.B1 + A2.B2]
                   [B2]
"""

import numpy as np

def add_matrices(A, B):
    
    p = A.shape[0];
    q = A.shape[1];
    
    M = np.zeros((p, q))
    for i in range(p):
        for j in range(q):
            M[i, j] = A[i, j] + B[i, j]                                   
            
    return M

def multiply(A, B):
    
    p = A.shape[0]
    r = B.shape[1]
    
    M = np.zeros((p, r))
    for i in range(p):
        for j in range(r):
            M[i, j] = A[i, 0] * B[0, j]
            
    return M
            
def matrix_mult(A, B):
    
    p = A.shape[0]
    q = A.shape[1]
    r = B.shape[1]
    
    if p == 0 or q == 0 or r == 0:
        return np.zeros((p, r))
    elif p >= 1 and q == 1:
        return multiply(A, B)
    else:
        
        A1 = A[:, :q // 2]
        A2 = A[:, q // 2:]
        B1 = B[:q // 2, :]
        B2 = B[q // 2:, :]
        
        A1B1 = matrix_mult(A1, B1)
        A2B2 = matrix_mult(A2, B2)
        
        return add_matrices(A1B1, A2B2)

A = np.matrix([[2, 3, 1, -3], [4, -2, 1, 2]])
B = np.matrix([[2, 3, 1], [4, -1, -5], [0, -6, 3], [1, -1, 1]])
print(matrix_mult(A, B))
    
# Test
print()

A = np.matrix([[2]])
B = np.matrix([[-2]])
print(matrix_mult(A, B))
print()

A = np.matrix([[2]])
B = np.matrix([[-2, 4, 5]])
print(matrix_mult(A, B))
print()

A = np.matrix([[2, 4, 5]])
B = np.matrix([[-2], [4], [5]])
print(matrix_mult(A, B))
print()

A = np.matrix([[2, 3, 1, -3]])
B = np.matrix([[2, 3, 1], [4, -1, -5], [0, -6, 3], [1, -1, 1]])
print(matrix_mult(A, B))
print()

A = np.matrix([[2], [3], [1], [-3]])
B = np.matrix([[2]])
print(matrix_mult(A, B))
print()

A = np.matrix([[2], [3], [1], [-3]])
B = np.matrix([[2, 3, 1]])
print(matrix_mult(A, B))
print()

A = np.matrix([[2, 3, 1, -3], [4, -2, 1, 2]])
B = np.matrix([[2], [4], [0], [1]])
print(matrix_mult(A, B))