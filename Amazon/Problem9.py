"""
Problem:  Is Sudoku Valid
Given an incomplete Sudoku configuration in terms of a 9x9  2-D square matrix(mat[][]) the task to check if the current configuration is valid or not where a 0 represents an empty block.
Note: Current valid configuration does not ensure validity of the final solved sudoku. 
Refer to this : https://en.wikipedia.org/wiki/Sudoku

Example 1:

Input: mat[][] = [
[3, 0, 6, 5, 0, 8, 4, 0, 0]
[5, 2, 0, 0, 0, 0, 0, 0, 0]
[0, 8, 7, 0, 0, 0, 0, 3, 1]
[0, 0, 3, 0, 1, 0, 0, 8, 0]
[9, 0, 0, 8, 6, 3, 0, 0, 5]
[0, 5, 0, 0, 9, 0, 6, 0, 0]
[1, 3, 0, 0, 0, 0, 2, 5, 0]
[0, 0, 0, 0, 0, 0, 0, 7, 4]
[0, 0, 5, 2, 0, 6, 3, 0, 0]
]
Output: 1
Explaination: It is possible to have a
proper sudoku.
Your Task:
You do not need to read input or print anything. Your task is to complete the function isValid() which takes mat[][] as input parameter and returns 1 if any solution is possible. Otherwise, returns 0.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(1)

Constraints:
0 ≤ mat[i][j] ≤ 9

"""

def isValid(mat):
        # code here
        
        import collections
        
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        boxes=collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                
                if mat[r][c]==0:
                    continue
               
                if mat[r][c] in rows[r] or mat[r][c] in cols[c] or mat[r][c] in boxes[(r//3,c//3)]:
                   return 0
            
                rows[r].add(mat[r][c])
                cols[c].add(mat[r][c])
                boxes[(r//3,c//3)].add(mat[r][c])
               
               
        return 1

mat= [
[3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0],
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0],
]

if isValid(mat):
    print(True)
else:
    print(False)