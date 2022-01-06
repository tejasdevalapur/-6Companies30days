"""
Problem Statement: Longest Mountain in Array
You may recall that an array arr is a mountain array if and only if:

    1. arr.length >= 3
    2. There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
        i. arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
       ii. arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. 
Return 0 if there is no mountain subarray.

 
Example 1:

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.

"""

def longestMountain(arr) :
        
        
        if len(arr)<3:
            return 0
          
        #State represents the stage of mountain.
        # 0-means we are starting to bulid the mountain
        # 1-means we are building the mountain in increasing order
        # 2-means we are building the mountain in decreasing order

        #length means the length of the mountain built so far

        state,length=0,1

        #keep track of the maximum mountain length
        maxLength=0
        
        for i in range(len(arr)-1):
            
            # if state in 0 or 1 means array is increasing and length is incremented by 1 
            if state in [0,1] and arr[i+1]>arr[i]:
                state,length=1,length+1
            # if state in 2 means we have already built the mountain and array is increasing hence we are building new mountain.
            # so length is equal to 1
            elif state ==2 and arr[i+1]>arr[i]:
                state,length=1,2
            # if state in 1 or 2 and array is decreasing means that we are in decreasing phase and need to calculate the maximum length
            elif state in [1,2] and arr[i+1]<arr[i]:
                state,length=2,length+1
                maxLength=max(maxLength,length)
            # we reintialize of state and length as we are starting to build the mountain
            else:
                state,length=0,1
        
        return maxLength


arr=[2,1,4,7,3,2,5]
print(longestMountain(arr))