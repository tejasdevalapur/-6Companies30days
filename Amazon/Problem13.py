"""
Problem : Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

import collections
def orangesRotting(grid):
        
        
        row,col=len(grid),len(grid[0])
        
        step=0
        
        dirs=[(-1,0),(0,1),(1,0),(0,-1)]
        
        rotten=collections.deque()
        
        fresh_set=set()
        
        
        for i in range(row):
            for j in range(col):
                
                if grid[i][j]==1:
                    fresh_set.add((i,j))
                elif grid[i][j]==2:
                    rotten.append([i,j,step])
       
        while rotten:
            
            x,y,step=rotten.popleft()
            
            for dx,dy in dirs:
                
                if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0])and grid[x+dx][y+dy]==1:
                    
                    grid[x+dx][y+dy]=2
                    fresh_set.remove((x+dx,y+dy))
                    rotten.append([x+dx,y+dy,step+1])
                    
        return step if not fresh_set else -1