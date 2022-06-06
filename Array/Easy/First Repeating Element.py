# Given an array arr[] of size n, 
# find the first repeating element. 
# The element should occurs more than once 
# and the index of its first occurrence should be the smallest.

# Example 1:                                                                                                   
# Input:
# n = 7
# arr[] = {1, 5, 3, 4, 3, 5, 6}
# Output: 2
# Explanation: 
# 5 is appearing twice and 
# its first appearence is at index 2 
# which is less than 3 whose first 
# occuring index is 3.
 
# Example 2:  
# Input:
# n = 4
# arr[] = {1, 2, 3, 4}
# Output: -1
# Explanation: 
# All elements appear only once so 
# answer is -1.

# Solution :- O(N),O(N)
n =int(input())
arr = [int(i) for i in input().split()]
count = {}
for i in arr:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
for i in range(n):
    if count[arr[i]] > 1:
        print(i+1)
        break
if i == n-1:
    print(-1)