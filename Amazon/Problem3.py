"""
Problem Statement:  IPL 2021 - Match Day 2 
Due to the rise of covid-19 cases in India, 
this year BCCI decided to organize knock-out matches in IPL rather than a league.
Today is matchday 2 and it is between the most loved team Chennai Super Kings and the most underrated team- Punjab Kings. 
Stephen Fleming, the head coach of CSK, analyzing the batting stats of Punjab. 
He has stats of runs scored by all N players in the previous season and he wants to find the maximum score for each
and every contiguous sub-list of size K to strategize for the game.

Example 1:

Input:
N = 9, K = 3
arr[] = 1 2 3 1 4 5 2 3 6
Output: 
3 3 4 5 5 5 6 
Explanation: 
1st contiguous subarray = {1 2 3} Max = 3
2nd contiguous subarray = {2 3 1} Max = 3
3rd contiguous subarray = {3 1 4} Max = 4
4th contiguous subarray = {1 4 5} Max = 5
5th contiguous subarray = {4 5 2} Max = 5
6th contiguous subarray = {5 2 3} Max = 5
7th contiguous subarray = {2 3 6} Max = 6
"""
from collections import deque
def max_of_subarrays(arr,n,k):
        '''
        you can use collections module here.
        :param a: given array
        :param n: size of array
        :param k: value of k
        :return: A list of required values 
        '''
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

