"""
Question8
Problem:Total Decoding Messages

A top secret message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
You are an FBI agent. You have to determine the total number of ways that message can be decoded, as the answer can be large return the answer modulo 109 + 7.
Note: An empty digit sequence is considered to have one decoding. It may be assumed that the input contains valid digits from 0 to 9 and If there are leading 0’s, extra trailing 0’s and two or more consecutive 0’s then it is an invalid string.

Example 1:

Input: str = "123"
Output: 3
Explanation: "123" can be decoded as "ABC"(123),
"LC"(12 3) and "AW"(1 23).
Example 2:

Input: str = "27"
Output: 1
Explanation: "27" can be decoded as "BG".

"""

def CountWays(s):
        n=len(s)
        count = [0] * (n + 1) # A table to store 
                           # results of subproblems 
        count[0] = 1
        count[1] = 1
        mod=1000000007
        
        if s[0] == '0':
            return 0
        for i in range(2, n + 1): 
    
            count[i] = 0; 
    
            # If the last digit is not 0, then last
            # digit must add to the number of words 
            if (s[i - 1] > '0'): 
                count[i] = count[i - 1]; 
    
            # If second last digit is smaller than 2
            # and last digit is smaller than 7, then
            # last two digits form a valid character 
            if (s[i - 2] == '1' or 
               (s[i - 2] == '2' and 
                s[i - 1] < '7') ): 
                count[i] =(count[i]%mod+ count[i - 2]%mod)%mod; 

        return count[n]; 


print(CountWays("123"))