# Union of two arrays can be defined as the common and distinct elements 
# in the two arrays.
# Given two sorted arrays of size n and m respectively, find their union.


# Example 1:

# Input: 
# n = 5, arr1[] = {1, 2, 3, 4, 5}  
# m = 3, arr2 [] = {1, 2, 3}
# Output: 1 2 3 4 5
# Explanation: Distinct elements including 
# both the arrays are: 1 2 3 4 5.
 

# Example 2:

# Input: 
# n = 5, arr1[] = {2, 2, 3, 4, 5}  
# m = 5, arr2[] = {1, 1, 2, 3, 4}
# Output: 1 2 3 4 5
# Explanation: Distinct elements including 
# both the arrays are: 1 2 3 4 5.
 

# Example 3:

# Input:
# n = 5, arr1[] = {1, 1, 1, 1, 1}
# m = 5, arr2[] = {2, 2, 2, 2, 2}
# Output: 1 2
# Explanation: Distinct elements including 
# both the arrays are: 1 2.

# Solution :- O(N+M),O(N+M)
n = int(input())
a = [int(i) for i in input().split()]
m = int(input())
b = [int(i) for i in input().split()]
arr = []
i =0
j = 0
while i<n and j<m:
    x = a[i]
    y =b[j]
    if x<y:
        arr.append(x)
        while i<n and a[i] == x:
            i+=1
    elif x == y:
        arr.append(x)
        while i<n and a[i] ==x:
            i+=1
        while j<m and b[j] == y:
            j+=1
            
    else:
        arr.append(y)
        while j<m and b[j] == y:
            j+=1
            
while i<n:
    x = a[i]
    arr.append(x)
    while i<n and a[i] == x:
        i+=1
        
while j<m:
    y = b[j]
    arr.append(y)
    while j<m and b[j] == y:
        j+=1

    
print(arr)