"""
Problem:Serialize and Deserialize a Binary Tree

Serialization is to store a tree in an array so that it can be later restored and Deserialization is reading
 tree back from the array. Now your task is to complete the function serialize which stores the tree 
 into an array A[ ] and deSerialize which deserializes the array to the tree and returns it.
Note: The structure of the tree must be maintained. Multiple nodes can have the same data.

Example 1:

Input:
      1
    /   \
   2     3
Output: 2 1 3
"""

def serialize(root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res=[]
        
        def dfs(node):
            
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)     
        

def deserialize(data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        values=data.split(",")
        
        self.i=0
        
        def dfs():
            
            if values[self.i]=="N":
                self.i+=1
                return
            
            node=TreeNode(int(values[self.i]))
            self.i+=1
            
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()
        