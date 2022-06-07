# Given an array of length N consisting of only 0s and 1s in random order.
# Modify the array to segregate 0s on left side and 1s on the right side of the array.

# Example 1:

# Input:
# N = 5
# arr[] = {0, 0, 1, 1, 0}
# Output: 0 0 0 1 1

# Example 2:

# Input:
# N = 4
# Arr[] = {1, 1, 1, 1}
# Output: 1 1 1 1
# Explanation: There are no 0 in the given array, 
# so the modified array is 1 1 1 1.
# Solution :- O(N),O(1)

n = int(input())
arr = [int(i) for i in input().split()]
count = 0
i = 0
while i < n-count:
    if arr[i] == 1:
        count+=1
        arr.pop(i)
    else:
        i+=1
for i in range(count):
    arr.append(1)
print(arr)