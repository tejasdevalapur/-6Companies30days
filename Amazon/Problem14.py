"""
Problem: Burning Tree 
Given a binary tree and a node called target. Find the minimum time required to burn the complete binary tree if the target is set on fire. It is known that in 1 second all nodes connected to a given node get burned. That is its left child, right child, and parent.

Example 1:

Input:      
          1
        /   \
      2      3
    /  \      \
   4    5      6
       / \      \
      7   8      9
                   \
                   10
Target Node = 8
Output: 7
Explanation: If leaf with the value 
8 is set on fire. 
After 1 sec: 5 is set on fire.
After 2 sec: 2, 7 are set to fire.
After 3 sec: 4, 1 are set to fire.
After 4 sec: 3 is set to fire.
After 5 sec: 6 is set to fire.
After 6 sec: 9 is set to fire.
After 7 sec: 10 is set to fire.
It takes 7s to burn the complete tree.

"""


def gep(node,val,level,arr):

    if node == None:
        return False,0,0

    a,b,c = gep(node.left,val,level+1,arr)        
    x,y,z = gep(node.right,val,level+1,arr) 

    if node.val == val:            
        arr[0] = max(arr[0],max(c,z)+1,level-1)
        return True,0,max(c,z)+1

    elif a:
        arr[0] = max(arr[0],z+b)            
        return True,b+1,max(c,z)+1

    elif x:
        arr[0] = max(arr[0],c+y)
        return True,y+1,max(c,z)+1

    return False,0,max(c,z)+1

def solve(self, A, B):

    arr = [0]
    a,b,c = gep(A,B,0,arr)
   
    return arr[0]+1