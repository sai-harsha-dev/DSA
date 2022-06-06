# Given an array Arr of N positive integers and another number X. 
# Determine whether or not there exist two elements in Arr whose sum is exactly X.

# Example 1:

# Input:
# N = 6, X = 16
# Arr[] = {1, 4, 45, 6, 10, 8}
# Output: Yes
# Explanation: Arr[3] + Arr[4] = 6 + 10 = 16
# Example 2:

# Input:
# N = 5, X = 10
# Arr[] = {1, 2, 4, 3, 6}
# Output: Yes
# Explanation: Arr[2] + Arr[4] = 4 + 6 = 10

# Solution :- O(N),O(N) 
# Hint :- similar to count number of pairs with given sum.

n,x = map(int,input().split())
arr = [int(i) for i in input().split()]
appear = {}
count = 0
for i in arr:
    diff=x-i
    if diff in appear:
        count+=appear[diff]
        print("True")
        break
    if i in appear:
        appear[i]+=1
        continue
    appear[i] = 1
if count < 1:
  print("False")