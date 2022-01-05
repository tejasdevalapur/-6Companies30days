"""
Question 15

Problem:Array Pair Sum Divisibility Problem 

Given an array of integers and a number k, write a function that returns true if given array can be divided into pairs such that sum of every pair is divisible by k.
 

Example 1 :

Input : arr = [9, 5, 7, 3], k = 6
Output: True
Explanation: {(9, 3), (5, 7)} is a 
possible solution. 9 + 3 = 12 is divisible
by 6 and 7 + 5 = 12 is also divisible by 6.
"""


def canPair(nuns, k):
		# Code here

        #if length of the array is odd then pairs cannot be formed
        if(len(nuns)==0 or len(nuns)==1):
            return 0
        dic = {}
        #Count the occurencess of remainder array element
        for i in range(len(nuns)):
            if(((nuns[i] % k) + k) % k in dic):
                dic[((nuns[i] % k) + k) % k]+=1
            else:
                dic[((nuns[i] % k) + k) % k]=1

        for x in dic:
            #If remiander is 0 then check if any odd number of occurences are present in the dictionary
            if(x==0):
                if(dic[x]%2!=0):
                    return 0

            #Check if remiander with current element divides the k into two halves
            elif(2*x==k):
                #if so then there must be even no of occurences of the remainder
                if(dic[x]%2!=0):
                    return 0
            else:
                if((k-x) in dic):
                    if(dic[x]!=dic[k-x]):
                        return 0
                else:
                    return 0
        return 1


nuns=[9, 5, 7, 3]
k = 6

if canPair(nuns,k):
    print(True) 
else:
    print(False)