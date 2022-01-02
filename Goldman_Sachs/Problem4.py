"""
Question4
Run Length Encoding
Given a string, Your task is to  complete the function encode that returns the run length encoded string for the given string.
eg if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6″.

Expected Time Complexity: O(N), N = length of given string.
Expected Auxiliary Space: O(1)

Constraints:
1<=length of str<=100
"""

def encode(arr):
    # Code here
    #Variable to count the number of characters
    counter=1
    # StringBuilder 
    encodedString=""
    # Variable to keep track of previous character
    prevChar=arr[0]

    for i in range(1,len(arr)):
        #If current character is same as previous character increment Counter by 1.
        #Else add the previous character and counter to the string Builder and update previous character and Counter
        if prevChar==arr[i]:
            counter+=1
        else:
            encodedString+=prevChar+str(counter)
            prevChar=arr[i]
            counter=1
    
    encodedString+=prevChar+str(counter)
    
    return encodedString


arr="aaaabbbbccc"

result=encode(arr)

print(result)