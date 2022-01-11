"""
Problem: Nuts and Bolts 
Given a set of N nuts of different sizes and N bolts of different sizes. There is a one-one mapping between nuts and bolts. Match nuts and bolts efficiently.

Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller.
The elements should follow the following order ! # $ % & * @ ^ ~ .

Example 1:

Input: 
N = 5
nuts[] = {@, %, $, #, ^}
bolts[] = {%, @, #, $ ^}
Output: 
# $ % @ ^
# $ % @ ^

 """

def sots(arr):
        n=len(arr)
        for i in range(n):
            min_indx=i
            for j in range(i+1,n):
                if arr[min_indx]>arr[j]:
                    min_indx=j
            arr[i],arr[min_indx]=arr[min_indx],arr[i]
        return arr
    
    
def matchPairs(nuts, bolts, n):
        print(sots(nuts))
        print(sots(bolts))

N = 5
nuts=['@', '%','$', '#', '^']
bolts=['%', '@', '#', '$', '^']
matchPairs(nuts, bolts, N)