"""
 Brackets in Matrix Chain Multiplication 
 Given an array p[] of length n used to denote the dimensions of a series of matrices such that dimension of i'th matrix is p[i] * p[i+1]. There are a total of n-1 matrices. Find the most efficient way to multiply these matrices together. 
The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications such that you need to perform minimum number of multiplications. There are many options to multiply a chain of matrices because matrix multiplication is associative i.e. no matter how one parenthesize the product, the result will be the same.


Example 1:

Input: 
n = 5
p[] = {1, 2, 3, 4, 5}
Output: (((AB)C)D)
Explaination: The total number of 
multiplications are (1*2*3) + (1*3*4) 
+ (1*4*5) = 6 + 12 + 20 = 38.
"""

import sys
 
 
# Function to find the most efficient way to multiply
# a given sequence of matrices
def matrixChainMultiplication(dims, i, j):
 
    # base case: one matrix
    if j <= i + 1:
        return 0
 
    # stores the minimum number of scalar multiplications (i.e., cost)
    # needed to compute matrix `M[i+1] … M[j] = M[i…j]`
    min = sys.maxsize
 
    # take the minimum over each possible position at which the
    # sequence of matrices can be split
 
    '''
        (M[i+1]) × (M[i+2]………………M[j])
        (M[i+1]M[i+2]) × (M[i+3…………M[j])
        …
        …
        (M[i+1]M[i+2]…………M[j-1]) × (M[j])
    '''
 
    for k in range(i + 1, j):
 
        # recur for `M[i+1]…M[k]` to get an `i × k` matrix
        cost = matrixChainMultiplication(dims, i, k)
 
        # recur for `M[k+1]…M[j]` to get an `k × j` matrix
        cost += matrixChainMultiplication(dims, k, j)
 
        # cost to multiply two `i × k` and `k × j` matrix
        cost += dims[i] * dims[k] * dims[j]
 
        if cost < min:
            min = cost
 
    # return the minimum cost to multiply `M[j+1]…M[j]`
    return min
 
 
# Matrix Chain Multiplication Problem
if __name__ == '__main__':
 
    # Matrix `M[i]` has dimension `dims[i-1] × dims[i]` for `i=1…n`
    # input is 10 × 30 matrix, 30 × 5 matrix, 5 × 60 matrix
    dims = [10, 30, 5, 60]
 
    print('The minimum cost is', matrixChainMultiplication(dims, 0, len(dims) - 1))