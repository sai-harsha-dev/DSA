# Given an array of positive and negative numbers. 
# Find if there is a subarray (of size at-least one) with 0 sum.

# Example 1:

# Input:
# 5
# 4 2 -3 1 6

# Output: 
# Yes

# Explanation: 
# 2, -3, 1 is the subarray 
# with sum 0.
# Example 2:

# Input:
# 5
# 4 2 0 1 6

# Output: 
# Yes

# Explanation: 
# 0 is one of the element 
# in the array so there exist a 
# subarray with sum 0.

# Solution :- O(N),O(N) ---->https://www.youtube.com/watch?v=8inhayLCCHs
n = int(input())
arr= [int(i) for i in input().split()]
prefix_sum = {arr[0]:1}
prev = arr[0]
for i in range(1,n):
    prev+=arr[i]
    if prev in prefix_sum:
        prefix_sum[prev]+=1
    else:
        prefix_sum[prev]=1
check = 0
for i in prefix_sum:
    if prefix_sum[i] > 1 or i == 0:
        check = 1
        break
if check == 1:    
    print("True")
else:
    print("false")
