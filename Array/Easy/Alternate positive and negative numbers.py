# Given an unsorted array Arr of N positive and negative numbers. 
# Your taskis to create an array of alternate positive and negative numbers 
# without changing the relative order of positive and negative numbers.
# Note: Array should start with positive number.
 
# Example 1:

# Input: 
# N = 9
# Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
# Output:
# 9 -2 4 -1 5 -5 0 -3 2
# Example 2:

# Input: 
# N = 10
# Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
# Output:
# 5 -5 2 -2 4 -8 7 1 8 0 

# Solution:- O(N),0(N)
n = int(input())
arr = [int(i) for i in input().split()]

pos = [] # To keep track of order of positive numbers
neg = [] # To keep track of order of negative numbers
for i in arr:
    if i>=0:
        pos.append(i)
    else:
        neg.append(i)
i = 0 # Places pairs of pos and neg number in arr
while i<len(pos) and i<len(neg):
    arr[2*i]= pos[i]
    arr[2*i+1] = neg[i]
    i+=1
j = 2*i # Starting index for left over pos or neg numbers,2*i since pos
        # and neg numbers are added in pairs
# K tracks index of next number to be added
# J Tracks index in arr where the number should be added
for k in range(i,len(pos)): # if there are more positive numbers than neg
    arr[j] = pos[k]
    j+=1 
for k in range(i,len(neg)): # if there are more neg than pos
    arr[j] = neg[k]
    j+=1
print(arr)