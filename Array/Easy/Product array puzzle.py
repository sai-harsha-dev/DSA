# Given an array nums[] of size n, construct a Product Array P 
# (of same size n) such that P[i] is equal to the 
# product of all the elements of nums except nums[i].

# Example 1:

# Input:
# n = 5
# nums[] = {10, 3, 5, 6, 2}
# Output:
# 180 600 360 300 900
# Explanation: 
# For i=0, P[i] = 3*5*6*2 = 180.
# For i=1, P[i] = 10*5*6*2 = 600.
# For i=2, P[i] = 10*3*6*2 = 360.
# For i=3, P[i] = 10*3*5*2 = 300.
# For i=4, P[i] = 10*3*5*6 = 900.

# Solution :-O(N),O(N)
# The tricky part here is to update the element in index with 0 ,  
# the different possibilities are :-
# 1)There is only one index with 0 element|2)There are more than one index's with 0 elemet
#   --------------------------------------------------------------------------------------
#   In this case it is enought to update  |  In this case whole array will be zero.
#   that specific element alone and the   |  since there are multiple zeroes, and
#   rest as 0(since product of whole array|  even with the first 0 element omited
#   will be zero, sice there is a 0       |  product will be zero.
#   in-beween).                           |  

n = int(input())
nums = [int(i) for i in input().split()]
op = []
zero = n+1
total = 1
left_product = 1
right_product= 1  

for i in range(n):
    if nums[i] == 0 and zero>n: # updates the first 0 element
        zero = i
    else:
        total = total*nums[i]   # Updates product not considering the first 0 element.

for i in range(n-1,-1,-1):
    right_product = right_product*nums[i] # calculted the product of array 
for i in range(n):
    if zero <= n:           # for case if 1 or multiple zero's is present
        if i == zero:
            op.append(total)
        else:
            op.append(0)
    else:                   # for array with no xero element present
        right_product = right_product//nums[i]
        update = right_product*left_product
        left_product*=nums[i]
        op.append(update)
        
print(op)