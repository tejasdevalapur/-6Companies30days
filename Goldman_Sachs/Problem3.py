"""
Question3

Count the subarrays having product less than k 

Given an array of positive numbers, the task is to find the number of possible contiguous subarrays having product less than a given number k.
Input : 
n = 4, k = 10
a[] = {1, 2, 3, 4}
Output : 
7
Explanation:
The contiguous subarrays are {1}, {2}, {3}, {4} 
{1, 2}, {1, 2, 3} and {2, 3} whose count is 7.
"""
def countSubArrayProductLessThanK(a, n, k):
        """
        Technique Used: Sliding Window Approach

        Task: Count the subarrays having product less than k.
        Approach:
            1.Consider two pointers start and end
            2.There are two cases to consider
                Case 1: if product is less than K then the subarraysCount will be end-start+1(No of elements in the subarray that is the window length)
                Case 2: if product is greater than K then we need to adjust our window.Hence we will divide the product with arr[start] and increment the start pointer by 1
        """
        
        
        product=1
        
        
        subArraysCount=0
        
        left=0
        
        for right in range(n):
            
            product*=a[right]
            
            while right <n and product>=k:
                product/=a[left]
                left+=1
            if product<k:
                subArraysCount+=1+(right-left)
                
        return subArraysCount

a=[1,2,3,4]
n=4
k=10

result=countSubArrayProductLessThanK(a,n,k)

print(result)