"""
Problem: Column name from a given column number

Given a positive integer, return its corresponding column title as appear in an Excel sheet.
Excel columns has a pattern like A, B, C, … ,Z, AA, AB, AC,…. ,AZ, BA, BB, … ZZ, AAA, AAB ….. etc. In other words, column 1 is named as “A”, column 2 as “B”, column 27 as “AA” and so on.

Example 1:

Input:
N = 28
Output: AB
Explanation: 1 to 26 are A to Z.
Then, 27 is AA and 28 = AB.
"""
def printString(n):

    # To store result (Excel column name)
    string = ["\0"] * MAX

    # To store current index in str which is result

    i = 0

    while n > 0:
        # Find remainder
        rem = n % 26

        # if remainder is 0, then a 
        # 'Z' must be there in output
        if rem == 0:
            string[i] = 'Z'
            i += 1
            n = (n / 26) - 1
        else:
            string[i] = chr((rem - 1) + ord('A'))
            i += 1
            n = n / 26
    string[i] = '\0'

    # Reverse the string and print result
    string = string[::-1]
    print("".join(string))


    printString(26)