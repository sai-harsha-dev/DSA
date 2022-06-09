# Given an array A of n positive numbers. 
# The task is to find the first Equilibium Point in the array. 
# Equilibrium Point in an array is a position such that the 
# sum of elements before it is equal to the sum of elements after it.

# Note: Retun the index of Equilibrium point. (1-based index)

# Example 1:

# Input: 
# n = 5 
# A[] = {1,3,5,2,2} 
# Output: 3 
# Explanation: For second test case 
# equilibrium point is at position 3 
# as elements before it (1+3) = 
# elements after it (2+2). 
 

# Example 2:

# Input:
# n = 1
# A[] = {1}
# Output: 1
# Explanation:
# Since its the only element hence
# its the only equilibrium point.
 
# Solution :-O(N),O(1) 
# youtube link :- https://www.youtube.com/watch?v=W-t1rjLxvQw&t=238s

# Explanation :- Equilibrium point = left_sum == right_sum
#                                  = left_sum = total_sum - left_sum
#                 since  right_sum = total_sum - left_sum
# Hence we need to find the index where left_sum = total_sum - left_sum

A =[int(i) for i in input().split()]
N = int(input())
Total = 0
if N == 1:
    print(1)
elif N == 2:
    print(-1)
else:
    for i in A:
        Total+=i
    left_sum = A[0]
    Total-=A[0]
    for i in range(1,N-1):
        Total-=A[i] # finds right_sum(right_sum = total- A[i]) at index i 
        if Total == left_sum: # checks if left_sum = total_sum - left_sum
            print(i+1)
        left_sum+=A[i] # Calculstes left sum at each index.
    print(-1)