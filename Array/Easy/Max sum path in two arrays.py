# Given two sorted arrays A and B of size M and N respectively. 
# Each array may have some elements in common with the other array. 
# Find the maximum sum of a path from the beginning of any array to 
# the end of any of the two arrays. We can switch from one array to 
# another array only at the common elements.Both the arrays are sorted.
# Note: Only one repeated value is considered in the valid path sum.

# Example 1:

# Input:
# M = 5, N = 4
# A[] = {2,3,7,10,12}
# B[] = {1,5,7,8}
# Output: 35
# Explanation: The path will be 1+5+7+10+12
# = 35.

# Example 2:

# Input:
# M = 3, N = 3
# A[] = {1,2,3}
# B[] = {3,4,5}
# Output: 15
# Explanation: The path will be 1+2+3+4+5=15.

# Solution :- O(N+M),O(1)
# Explanation :-1)The hint here is that the arrays are sorted, there we can be sure
#                that if an number at an index in arr1 is greater than the number
#                at an index in arr2 then, there is chance that the same number can
#                can appear in arr2 at an later index, sice the arrays are sorted
#               
#               2)So to find the common points in array we can have to pointers for 
#                to show the point till which index in each array we covered, and 
#                increamnent the pointer with lower value element till we find same
#                element. And at same time keep track of total of two arrays till  
#                those particular index for the array.
#
#               3)When the common point is found we check which array has highest 
#                 sum and add it to the final answer.
m = int(input())
arr1 = [int(i) for i in input().split()]
n = int(input())
arr2 = [int(i) for i in input().split()]
arr1_total = 0                      # Tracks arr1 one sub-sum
arr2_total = 0                      # Tracks arr2 one sub-sum
i = 0                               # Tracks arr1 last traversed index
j = 0                               # Tracks arr2 last traversed index
total = 0                           # Final heighest total 
while i < m and j < n:
    if arr1[i] == arr2[j]:          # At common point check which sub-sum is greated
                                    # and add it final answer
        total+=arr1[i]              # Add common point to the total before updating
        if arr2_total>=arr1_total:
            total+=arr2_total
        else:
            total+=arr1_total
        arr2_total = 0              # Start tracking new sub sum
        arr1_total = 0              # Start tracking new sub sum
        i+=1                        # Move the pointer from common value index in arr1
        j+=1                        # Move the pointer from common value index in arr2
    elif arr1[i] > arr2[j]:         # Checks in which arr index has higher value 
        arr2_total+=arr2[j]
        j+=1
    else:
        arr1_total+=arr1[i]
        i+=1
while j<n:                          # To complete subsum for left over indexes
    arr2_total+=arr2[j]
    j+=1
while i<m:
    arr1_total+=arr1[i]
    i+=1
if arr2_total>=arr1_total:          # Update total for left over indexes
    total+=arr2_total
else:
    total+=arr1_total
print(total)