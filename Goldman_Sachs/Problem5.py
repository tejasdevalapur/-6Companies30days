"""
Question 5

Problem:Ugly Numbers

Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included. Write a program to find Nth Ugly Number.

Example 1:

Input:
N = 10
Output: 12
Explanation: 10th ugly number is 12.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

"""

def getNthUglyNo(n):

     # Ugly number is a number whose factors are 2,3,5 only which means if 2*x or 3*x or 5*x then x should be a number 
     # which has prime factors of 2,3,5 only.
     # 2 factors list=[2,4,6, 8,10,12,14,16,18,20]
     # 3 factors list=[3,6, 9, 12,15,18,21,24,27,30]
     # 5 factors list=[5,10,15,20,25,30,35,40,45,50]
     # Ugly numbers=  [1,2,3,4,5,6,8,9,10,12,15,..](numbers are multiple of 2,3,5 only)
		# code here
        ugly=[0]*n
        
        #As 1 is included by Convention
        ugly[0]=1
        
        #Intialize the prime factors
        multiple_of_two=2
        multiple_of_three=3
        multiple_of_five=5
        
        #i2,i3,i5 are the incides of 2,3,5 respectively
        i2=i3=i5=0
        
        for index in range(1,n):
            
            ugly[index]=min(multiple_of_two,multiple_of_three,multiple_of_five)
            
            
            if ugly[index]==multiple_of_two:
                #increment i2 and update next multiple_of_two
                i2=i2+1
                multiple_of_two=ugly[i2]*2
            if ugly[index]==multiple_of_three:
                #increment i2 and update next multiple_of_two
                i3=i3+1
                multiple_of_three=ugly[i3]*3
            if ugly[index]==multiple_of_five:
                #increment i2 and update next multiple_of_two
                i5=i5+1
                multiple_of_five=ugly[i5]*5
        
        return ugly[-1]

n=11
result=getNthUglyNo(n)
print(result)
