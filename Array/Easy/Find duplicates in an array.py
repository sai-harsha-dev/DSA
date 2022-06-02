# Given an array a[] of size N which contains elements from 0 to N-1,
# you need to find all the elements occurring more than once in the given array.

# Example 1:

# Input:
# N = 4
# a[] = {0,3,1,2}
# Output: -1
# Explanation: N=4 and all elements from 0
# to (N-1 = 3) are present in the given
# array. Therefore output is -1.
# Example 2:

# Input:
# N = 5
# a[] = {2,3,1,2,3}
# Output: 2 3 
# Explanation: 2 and 3 occur more than once
# in the given array.

# Solution :- 0(N),0(N)

arr =[int(i) for i in input().split()]
n = int(input())
count = [0 for i in range(n)]    	
n= 0
for i in arr:
    count[i]+=1
for i in range(len(count)):
    if count[i] > 1:
        count[n] = i
        n+=1
if n == 0:
    print([-1])
print(count[:n])
