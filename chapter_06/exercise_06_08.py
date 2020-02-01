# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 08:15:55 2020

@author: Pshypher

Matrix multiplication algorithm implemented via recursion by decomposing the 
input matrices as follows
    
    AB = [A1]
         ---- . [B1 | B2]
         [A2]                            
"""
import numpy as np

def add_matrices(A, B, operator):
    
    p = A.shape[0]
    q = A.shape[1]
    
    M = np.zeros((p, q))
    for i in range(p):
        for j in range(q):
            M[i, j] = A[i, j] + B[i, j]                                        
            
    return M

def multiply(A, B):
    
    p = A.shape[0]
    q = A.shape[1]
    r = B.shape[1]
    
    M = np.zeros((p, r))
    for i in range(q):
        M[0, 0] += A[0, i] * B[i, 0]
        
    return M        

def matrix_mult(A, B):
    
    p = A.shape[0]
    q = A.shape[1]
    r = B.shape[1]
    
    if p == 0 or q == 0 or r == 0:
        return np.zeros((p, r))
    elif p == 1 and q == 1 and r == 1:
        return np.matrix([[A[0, 0] * B[0, 0]]])
    elif p == 1 and q > 1 and r == 1:
        return multiply(A, B)
    else:
        
        A1 = A[:p // 2, :]
        A2 = A[p // 2:, :]
        B1 = B[:, :r // 2]
        B2 = B[:, r // 2:]
        
        C11 = matrix_mult(A1, B1)
        C12 = matrix_mult(A1, B2)
        C21 = matrix_mult(A2, B1)
        C22 = matrix_mult(A2, B2)
        
        return np.vstack((np.hstack((C11, C12)),
                          np.hstack((C21, C22))))
        
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
