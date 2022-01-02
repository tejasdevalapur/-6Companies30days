"""
Question 6

Problem:Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

"""
def gcdOfStrings(str1: str, str2: str) -> str:

        #Greatest Common Divisor of the string is prefix of each string

        #if both strings are same length return the same string
        if len(str1) == len(str2):
            return str1 if str1==str2 else ''
        else:
            #if str1 is smaller than str2 then swap the strings
            if len(str1) < len(str2):
                str1,str2 = str2,str1
            #If the str2 length of substring of str1 is equal to str2 then recur on substring of str1 (length of str2)
            if str1[:len(str2)] == str2:
                return gcdOfStrings(str1[len(str2):],str2)
            else:
                return ''

str1="ABCABC"
str2 = "ABC"

result =gcdOfStrings(str1,str2)

print(result)