"""
Question
Problem: Number following a pattern
Given a pattern containing only I's and D's. I for increasing and D for decreasing.
Devise an algorithm to print the minimum number following that pattern.
Digits from 1-9 and digits can't repeat.

Example 1:

Input:
D
Output:
21
Explanation:
D is meant for decreasing,
So we choose the minimum number
among 21,31,54,87,etc.
"""

def PrintMinNumberForPattern(Strr):
     
    # Take a List to work as Stack
    stack = []
 
    # String for storing result
    res = ''
 
    # run n+1 times where n is length
    # of input sequence, As length of
    # result string is always 1 greater
    for i in range(len(Strr) + 1):
 
        # Push number i+1 into the stack
        stack.append(i + 1)
 
        # If all characters of the input
        # sequence are processed or current
        # character is 'I
        if (i == len(Strr) or Strr[i] == 'I'):
 
            # Run While Loop Until stack is empty
            while len(stack) > 0:
                 
                # pop the element on top of stack
                # And store it in result String
                res += str(stack.pop())
                
                 
    # Print the result
    print(res)
 

PrintMinNumberForPattern("IDID")