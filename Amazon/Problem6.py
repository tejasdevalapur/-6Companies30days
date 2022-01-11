"""
Problem:  Maximum of all subarrays of size k
Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous subarray of size K.

Example 1:

Input:
N = 9, K = 3
arr[] = 1 2 3 1 4 5 2 3 6
Output: 
3 3 4 5 5 5 6 
"""

from collections import deque
def max_of_subarrays(arr,n,k):
        #code here
        res = []
        
        d = deque()
        
        for i in range(k):
            while len(d) and arr[i]>=arr[d[-1]]: # -1 repesents right end of deque
                d.pop()
            d.append(i)
    
        for i in range(k,n):
            
            res.append (arr[d[0]])
            while len(d) and d[0]<=i-k:
                d.popleft()
            while len(d) and arr[i]>=arr[d[-1]]:
                d.pop()
            d.append(i)
    
        res.append (arr[d[0]])
        d.popleft()
        return res
N = 9
K = 3
arr=[1 ,2, 3 ,1 ,4 ,5, 2, 3, 6]
print(max_of_subarrays(arr,N,K))
