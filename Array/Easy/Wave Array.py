# Given a sorted array arr[] of distinct integers. 
# Sort the array into a wave-like array and return it.
# In other words, arrange the elements into a sequence 
# such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
# If there are multiple solutions, find the lexicographically smallest one.

# 	Example 1:
# 	Input:
# 	n = 5
# 	arr[] = {1,2,3,4,5}

# 	Output: 2 1 4 3 5
# 	Explanation: Array elements after sorting it in wave form are 2 1 4 3 5.

# 	Example 2:
# 	Input:
# 	n = 6
# 	arr[] = {2,4,7,8,9,10}

# 	Output: 4 2 8 7 10 9
# 	Explanation: Array elements after sorting it in wave form are 4 2 8 7 10 9.

# 	Sol :- O(N),O(1)
n = int(input())
a = [int(i) for i in input().split()]
odd = n%2
odd +=1
for i in range(0,n-odd,2):
		a[i],a[i+1] = a[i+1],a[i]
for i in range(n-1):
		print(a[i],end=" ")
print(a[n-1])
