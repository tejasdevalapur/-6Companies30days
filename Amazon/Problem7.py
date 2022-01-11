"""
Problem :  First non-repeating character in a stream 

Given an input stream of A of n characters consisting only of lower case alphabets. 
The task is to find the first non repeating character, each time a character is inserted to the stream. 
If there is no such character then append '#' to the answer.
 
Example 1:

Input: A = "aabc"
Output: "a#bb"
Explanation: For every character first non
repeating character is as follow-
"a" - first non-repeating character is 'a'
"aa" - no non-repeating character so '#'
"aab" - first non-repeating character is 'b'
"aabc" - first non-repeating character is 'b'
""" 


def FirstNonRepeating(string):

    if not string:
        return ''

    #Intialize a count array of size 26
    count=[0]*26

    #Initailize a Queue
    queue=[]

    # Output String
    output=''

    #Loop through each character in the given string

    for char in string:

        # Append the character to the queue
        queue.append(char)

        #Count the frequency of occurrences of the character in the given string
        
        count[ord(char)-ord('a')]+=1


        # Check if the frequency of front character in the queue is greater than the 1 then pop the character from the queue
        # Else the front character is the first nonrepeating character in the stream. 

        while queue:

            if count[ord(queue[0])-ord('a')]>1:
                queue.pop(0)
            else:
                output+=queue[0]
                break
        # queue is empty then no repeating character
        if not queue:
            output+='#'

    
    return output
                

string="aabc"

print(FirstNonRepeating(string))