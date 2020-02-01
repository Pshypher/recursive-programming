# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 07:47:44 2020

@author: Pshypher

Computes the product of two matrices using strassen's matrix multiplication
algorithm.

"""

import numpy as np

ADD = '+'
SUBTRACT = '-'

def pad(M, n):
    
    p = M.shape[0]
    q = M.shape[1]
        
    s = n - p
    t = n - q

    O = np.zeros((s, q))
    M = np.vstack((M, O))
    
    O = np.zeros((n, t))
    M = np.hstack((M, O))
    
    return M
    
def add_matrices(A, B, operator):
    
    p = A.shape[0];
    q = A.shape[1];
    
    M = np.zeros((p, q))
    for i in range(p):
        for j in range(q):
            if operator == ADD:
                M[i, j] = A[i, j] + B[i, j]
            else:
                M[i, j] = A[i, j] - B[i, j]                                        
            
    return M
        
    
def multiply_matrices(A, B):
    
    p = A.shape[0]
    q = A.shape[1]
    r = B.shape[0]
    s = B.shape[1]
    
    if (p == 1 and q == 1) and (r == 1 and s == 1):
        return np.matrix([[A[0, 0] * B[0, 0]]])
    else:
        
        A11 = A[:p // 2, :q // 2]
        A12 = A[:p // 2, q // 2:]
        A21 = A[p // 2:, :q // 2]
        A22 = A[p // 2:, q // 2:]
        B11 = B[:r // 2, :s // 2]
        B12 = B[:r // 2, s // 2:]
        B21 = B[r // 2:, :s // 2]
        B22 = B[r // 2:, s // 2:]
        
        M1 = multiply_matrices(add_matrices(A11, A22, ADD), 
                               add_matrices(B11, B22, ADD))
        M2 = multiply_matrices(add_matrices(A21, A22, ADD), B11)
        M3 = multiply_matrices(A11, add_matrices(B12, B22, SUBTRACT))
        M4 = multiply_matrices(A22, add_matrices(B21, B11, SUBTRACT))
        M5 = multiply_matrices(add_matrices(A11, A12, ADD), B22)
        M6 = multiply_matrices(add_matrices(A21, A11, SUBTRACT), 
                               add_matrices(B11, B12, ADD))
        M7 = multiply_matrices(add_matrices(A12, A22, SUBTRACT),
                               add_matrices(B21, B22, ADD))
        
        C11 = add_matrices(
                add_matrices(
                        add_matrices(M1, M4, ADD), M5, SUBTRACT),
                        M7, ADD)
        C12 = add_matrices(M3, M5, ADD)
        C21 = add_matrices(M2, M4, ADD)
        C22 = add_matrices(
                add_matrices(
                        add_matrices(M1, M2, SUBTRACT), M3, ADD), 
                        M6, ADD)
        
        return np.vstack((np.hstack((C11, C12)), 
                          np.hstack((C21, C22))))
        
def strassen_matrix_mult(A, B):
    
    p = A.shape[0]
    q = A.shape[1]
    r = B.shape[1]
    
    m = max(p, q, r)
    k = 0
    n = 2 ** k
    
    while n < m:
        k = k + 1
        n = 2 ** k
        
    A = pad(A, n)
    B = pad(B, n)        
    
    M = multiply_matrices(A, B)
    return M[0:p, 0:r]

A = np.matrix([[2, 3, 1, -3], [4, -2, 1, 2]])
B = np.matrix([[2, 3, 1], [4, -1, -5], [0, -6, 3], [1, -1, 1]])
print(strassen_matrix_mult(A, B))

# Test
print()

A = np.matrix([[2]])
B = np.matrix([[-2]])
print(strassen_matrix_mult(A, B))
print()

A = np.matrix([[2]])
B = np.matrix([[-2, 4, 5]])
print(strassen_matrix_mult(A, B))
print()

A = np.matrix([[2, 4, 5]])
B = np.matrix([[-2], [4], [5]])
print(strassen_matrix_mult(A, B))
print()

A = np.matrix([[2, 3, 1, -3]])
B = np.matrix([[2, 3, 1], [4, -1, -5], [0, -6, 3], [1, -1, 1]])
print(strassen_matrix_mult(A, B))
print()

A = np.matrix([[2], [3], [1], [-3]])
B = np.matrix([[2]])
print(strassen_matrix_mult(A, B))
print()

A = np.matrix([[2], [3], [1], [-3]])
B = np.matrix([[2, 3, 1]])
print(strassen_matrix_mult(A, B))
print()

A = np.matrix([[2, 3, 1, -3], [4, -2, 1, 2]])
B = np.matrix([[2], [4], [0], [1]])
print(strassen_matrix_mult(A, B))