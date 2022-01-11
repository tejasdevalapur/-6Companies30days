"""
Problem:  Count ways to N'th Stair(Order does not matter)

There are N stairs, and a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top (order does not matter).
Note: Order does not matter means for n=4 {1 2 1},{2 1 1},{1 1 2} are considered same.

Example 1:

Input:
N = 4
Output: 3
Explanation: You can reach 4th stair in
3 ways.
3 possible ways are:
1, 1, 1, 1
1, 1, 2
2, 2
"""


def countWays(m):
        
        mod = 1000000007
        # code here
        
        dp=[0]*(m+1)
        
        dp[0]=1
        dp[1]=1
        
        for i in range(2,m+1):
            
            dp[i]=1+min(dp[i-1],dp[i-2])
        
        return dp[m]

n=4
print(countWays(n))