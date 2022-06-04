# Given an array having both positive and negative integers. 
# The task is to compute the length of the largest subarray with sum 0.

# Example 1:

# Input:
# N = 8
# A[] = {15,-2,2,-8,1,7,10,23}
# Output: 5
# Explanation: The largest subarray with
# sum 0 will be -2 2 -8 1 7.

# Solution :- O(N),O(N) 
# Hint :- same prefix sum concept, additionally
# update the farthest appereaded index for every  repeated element
# in prefix sum (except 0 [because it means the sum oof whole array till
# that point is 0])   and compare and update the lenght.

n = int(input())
arr = [int(i) for i in input().split()]
prefix_sum = []
# to create prefix sum array
prefix_sum.append(arr[0])
for i in range(n-1):
    prefix_sum.append(prefix_sum[i]+arr[i+1])
lenght = 0 # to keep track of larget lenght subarray
# dict which keeps track of farthest index the element apperared in prefix sum
prev = {}  
# checks if prefix_sum = 0 or prefix_sum element repeated
for i in range(len(prefix_sum)):
    if prefix_sum[i] == 0 :
        if i+1 > lenght:
            lenght = i+1 # because 0 means the sum of whole array till that point is 0
            continue
    if prefix_sum[i] in prev : # checks the lenght of subarray when element repeated
        if i - prev[prefix_sum[i]]  >lenght:
            lenght = i - prev[prefix_sum[i]]
    else:  # updates farthest index when the element first appeared
        prev[prefix_sum[i]]=i
print(lenght)