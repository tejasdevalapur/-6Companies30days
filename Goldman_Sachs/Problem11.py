"""
Question 11
Problem:Find Missing And Repeating 

Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.

Example 1:

Input:
N = 2
Arr[] = {2, 2}
Output: 2 1
Explanation: Repeating number is 2 and 
smallest positive missing number is 1.
"""

def findTwoElement(arr, n): 
        # code here
        
        Map={}
        
        a,b=0,0
        
        for i in range(1,n+1):
            Map[i]=0
        
        for num in arr:
            Map[num]=Map.get(num,0)+1
        
        for key in Map:
            if Map[key]==0:
                a=key
            elif Map[key]>1:
                b=key
        
        return b,a

N=2
arr=[2,2]

print(findTwoElement(arr,N))