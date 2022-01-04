"""
Question 14

Problem:Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105

"""

def minSubArrayLen(target, nums):
        
        
        result=len(nums)+1
        left=0
        totalSum=0
        for right in range(len(nums)):
            totalSum+=nums[right]
            
            while totalSum>=target:
                result=min(result, right-left+1)
                totalSum-=nums[left]
                left+=1
            
        return result if result<=len(nums) else 0
                

nums=[2,3,1,2,4,3]
target=7
print(minSubArrayLen(target, nums))
