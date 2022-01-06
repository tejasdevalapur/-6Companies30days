"""
Problem Statement:Maximum Profit
In the stock market, a person buys a stock and sells it on some future date. Given the stock prices of N days in an array A[ ] and a positive integer K, find out the maximum profit a person can make in at-most K transactions. A transaction is equivalent to (buying + selling) of a stock and new transaction can start only when the previous transaction has been completed.


Example 1:

Input: K = 2, N = 6
A = {10, 22, 5, 75, 65, 80}
Output: 87
Explaination: 
1st transaction: buy at 10 and sell at 22. 
2nd transaction : buy at 5 and sell at 80.
Example 2:

Input: K = 3, N = 4
A = {20, 580, 420, 900}
Output: 1040
Explaination: The trader can make at most 2 
transactions and giving him a profit of 1040.
Example 3:

Input: K = 1, N = 5
A = {100, 90, 80, 50, 25}
Output: 0
Explaination: Selling price is decreasing 
daily. So seller cannot have profit.

Expected Time Complexity: O(N*K)
Expected Auxiliary Space: O(N*K)

"""

def trade_at_most_k_times( k, prices):
    n = len(prices)
    ## Base case:
	# Price sequence is empty, we can do nothing : )
    if n == 0:
        
        return 0


	## General case:

	# DP[ k ][ d ] = max profit on k, d
	# where k stands for k-th transaction, d stands for d-th trading day.
    dp = [ [ 0 for _ in range(n)] for _ in range(k+1) ]


	# Update by each transction as well as each trading day
    for trans_k in range(1, k+1):

		# Balance before 1st transaction must be zero
		# Buy stock on first day means -prices[0]
        cur_balance_with_buy = 0 - prices[0]
        for day_d in range(1, n):

			# Either we have finished all k transactions before, or just finished k-th transaction today
            dp[trans_k][day_d] = max( dp[trans_k][day_d-1], cur_balance_with_buy + prices[day_d] )
            
			# Either keep holding the stock we bought before, or just buy in today
            cur_balance_with_buy = max(cur_balance_with_buy, dp[trans_k-1][day_d-1] - prices[day_d] )
    return dp[k][n-1]

def maxProfit( k, prices):
        
	print(trade_at_most_k_times(k, prices))



prices= [10, 22, 5, 75, 65, 80]
k=2

maxProfit(k, prices)

