# Given a array of N strings, find the longest common prefix among 
# all strings present in the array.

# Example 1:

# Input:
# N = 4
# arr[] = {geeksforgeeks, geeks, geek,
#          geezer}
# Output: gee
# Explanation: "gee" is the longest common
# prefix in all the given strings.
# Example 2:

# Input: 
# N = 2
# arr[] = {hello, world}
# Output: -1
# Explanation: There's no common prefix
# in the given strings.

# Solution:- O(N*len(max(arr)),O(len(max(arr)))
# Explanation :- Inorder for a a sub-string to be prefix it must be a substring of 
#                of smallest string in that array.Hence it id enough if we check
#                if a substring of smallest string is present in all the elements 
#                in a array

n = int(input())
arr = [i for i in input.split()]
small_str = arr[0]
for i in arr:                    # to find the smallest string
    if len(i) <= len(small_str):
        small_str= i         
count=len(small_str)            # tracks the min no.of elements of smallest
                                # string present in all element
for i in arr:
    for j in range(count):
        if small_str[j] != i[j]:# Check the fist index when string elements 
                                # do not match
            count = j
            break
if count == 0:                  # Since 0 elements of smallest string were 
                                # common in all element no common prefix
    print(-1)
else:
    print(small_str[:count])    # Common substring of smallest string present in 
                                # in all elements , i.e. commmon prefix.