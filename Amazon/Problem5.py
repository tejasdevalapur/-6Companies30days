""" 
Problem: Phone directory
Given a list of contacts contact[] of length n where each contact is a string which exist in a phone directory 
and a query string s. The task is to implement a search query for the phone directory. Run a search query for 
each prefix p of the query string s (i.e. from  index 1 to |s|) that prints all the distinct contacts which have 
the same prefix as p in lexicographical increasing order. Please refer the explanation part for better understanding.

Note: If there is no match between query and contacts, print "0".

Example 1:

Input: 
n = 3
contact[] = {"geeikistest", "geeksforgeeks", 
"geeksfortest"}
s = "geeips"
Output:
geeikistest geeksforgeeks geeksfortest
geeikistest geeksforgeeks geeksfortest
geeikistest geeksforgeeks geeksfortest
geeikistest
0
0
Explaination: By running the search query on 
contact list for "g" we get: "geeikistest", 
"geeksforgeeks" and "geeksfortest".
By running the search query on contact list 
for "ge" we get: "geeikistest" "geeksforgeeks"
and "geeksfortest".
By running the search query on contact list 
for "gee" we get: "geeikistest" "geeksforgeeks"
and "geeksfortest".
By running the search query on contact list 
for "geei" we get: "geeikistest".
No results found for "geeip", so print "0". 
No results found for "geeips", so print "0".
Your Task:
Youd do not need to read input or print anything. Your task is to complete the function displayContacts() which takes n, contact[ ] and s as input parameters and returns a list of list of strings for required prefixes. If some prefix has no matching contact return "0" on that list.

Expected Time Complexity: O(|s| * n * max|contact[i]|)
Expected Auxiliary Space: O(n * max|contact[i]|)
"""

import collections

class TrieNode:
    
    def __init__(self):
        self.children=collections.defaultdict(TrieNode)
        self.is_word=False
        
        
class Trie:
    
    def __init__(self):
        self.root=TrieNode()
        self.result=[]

        
    def insert(self,word):
        current=self.root
        
        for letter in word:
             current=current.children[letter]
        current.is_word=True
        current.word=word
        

    #   Do DFS on all on the each prefix of given string s
    def getAllPrefix(self,current,prefix,temp):
        
        if current.is_word:
            temp.append(prefix)
            
        
        for i in range(ord('a'),ord('z')+1):
            letter=chr(i)
            next=current.children.get(letter)
            
            if next is not None:
                self.getAllPrefix(next,prefix+letter,temp)
                
        return temp
            
    def startsWith(self,string):
        prev=self.root
        prefix=""
        count=0
        for i in range(0,len(string)):
            
            prefix+=string[i]
            
            lastchar=prefix[i]
            
            
            current=prev.children.get(lastchar)
            
            if current is None:
                self.result.append([0])
                break
            
            res=self.getAllPrefix(current,prefix,[])
            
            self.result.append(res)
            count+=1
           
            prev=current
        
        #Append '0' for the no match prefix of the given string s
        while count<len(string)-1:
            self.result.append([0])
            count+=1
        return self.result
       
                

def displayContacts(n, contact, s):
        # code here
        
        t=Trie()
        
        for word in contact:
                t.insert(word)
        
        result=t.startsWith(s)
        
        print(result)
        
        
n = 3
contact=["geeikistest", "geeksforgeeks", 
"geeksfortest"]
s = "geeips"

displayContacts(n,contact,s)