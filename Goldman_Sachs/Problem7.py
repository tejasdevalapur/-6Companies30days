"""
Question 7

Problem:Distributing M items in a circle of size N starting from K-th position
M items are to be delivered in a circle of size N. Find the position where the M-th item will be delivered if we start from a given position K. Note that items are distributed at adjacent positions starting from K.
Examples : 
 

Input : N = 5 // Size of circle
        M = 2 // Number of items
        K = 1 // Starting position
Output : 2
The first item will be given to 1st 
position. Second (or last) item will 
be delivered to 2nd position

Input : N = 5 
        M = 8 
        K = 2
Output : 4
The last item will be delivered to 
4th position
"""


def lastPosition(n,m,k):

    if m<=n-k+1:
        return m+k-1

    m=m-(n-k+1)

    if m%n==0:
        return n
    else:
        return m%n
    
"""

1-->2-->3-->4-->5
1   2   3   4   5

"""

n = 5
m = 2
k = 1
print (lastPosition(n, m, k))