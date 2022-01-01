"""
Print Anagrams Together 
Q1)Given an array of strings, return all groups of strings that are anagrams. The groups must be created in order of their appearance in the original array. Look at the sample case for clarification.

Example 1:

Input:
N = 5
words[] = {act,god,cat,dog,tac}
Output: 
god dog
act cat tac
Explanation:
There are 2 groups of
anagrams "god", "dog" make group 1.
"act", "cat", "tac" make group 2.

"""

def Anagrams(words):

    countAnagrams ={}

    for word in words:

        key=''.join(sorted(word))

        if key in countAnagrams.keys():
            countAnagrams[key].append(word)
        else:
            countAnagrams[key]=[]
            countAnagrams[key].append(word)
    
    groupAnagrams =[]

    for key,value in countAnagrams.items():
        groupAnagrams.append(value)
    
    return groupAnagrams



words=["act","god","cat","dog","tac"]

result=Anagrams(words)

for word in sorted(result):
    print(word,end=" ")
print()

"""
Time Complexity: O(N*S*logN) where S is length of the string
Space Complexity: O(N*S)
"""
