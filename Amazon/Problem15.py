"""
Problem:  Delete N nodes after M nodes of a linked list
Given a linked list, delete N nodes after skipping M nodes of a linked list until the last of the linked list. 

Example:
Input:
2
8
2 1
9 1 3 5 9 4 10 1
6
6 1
1 2 3 4 5 6

Output: 
9 1 5 9 10 1
1 2 3 4 5 6
"""

def skipMdeleteN(head, M, N):
        # Code here
        
        curr=head
        
        while curr and curr.next:
            for i in range(M-1):
                if curr and curr.next:
                    curr=curr.next
                
            for i in range(N):
                if curr and curr.next:
                    curr.next=curr.next.next
            curr=curr.next
        return head