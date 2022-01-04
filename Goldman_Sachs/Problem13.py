"""
Question 13

Problem:Decode the string

An encoded string (s) is given, the task is to decode it. The pattern in which the strings were encoded were as follows
original string: abbbababbbababbbab 
encoded string : 3[a3[b]1[ab]]

Example 1:

Input: s = 1[b]
Output: b
Explaination: 'b' is present only one time.


"""


def decodedString(s):
        # code here
        stack=[]
        currentString=''
        currentNumber=0
        
        for char in s:
            
            if char=='[':
                stack.append(currentString)
                stack.append(currentNumber)
                currentString=''
                currentNumber=0
            elif char==']':
                num=stack.pop()
                previousString=stack.pop()
                currentString=previousString+num*currentString
            elif char.isdigit():
                currentNumber=currentNumber*10+int(char)
            else:
                currentString+=char
        
        return currentString


s=input()

decoded_String=decodedString(s)
print(decoded_String)
