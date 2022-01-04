"""
Question 12

Problem: Find total number of Squares in a N*N chessboard

Examples: 

Input: n = 2
Output: 5 (4 squares of 1 unit + 1 square of 2 units)

Input: n = 3
Output: 14 (9 squares of 1 unit + 4 square of 2 units 
                                + 1 square of 1 unit) 
"""

def countSquares(n):

    if n == 0 or n == 1:
        return n
    
    totalSquares=0

    for i in range(1,n+1):

        totalSquares+=(i*i)
    
    return totalSquares


n=int(input('Enter the number'))

result=countSquares(n)

print('Total number of squares in {n}*{n} chessboard is {result}'.format(n=n, result=result))



    