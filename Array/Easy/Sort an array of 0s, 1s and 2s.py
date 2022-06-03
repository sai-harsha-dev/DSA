# Given an array of size N containing only 0s, 1s, and 2s; 
# sort the array in ascending order.

# 	Example 1:
# 	Input: 
# 	N = 5
# 	arr[]= {0 2 1 2 0}

# 	Output:
# 	0 0 1 2 2
# 	Explanation:
# 	0s 1s and 2s are segregated 
# 	into ascending order.

# 	Example 2:
# 	Input: 
# 	N = 3
# 	arr[] = {0 1 0}

# 	Output:
# 	0 0 1
# 	Explanation:
# 	0s 1s and 2s are segregated 
# 	into ascending order.

# 	Sol :- O(N),O(1)
n = int(input())
arr = [int(i) for i in input().split()]
one =[0, 0, 0]
for i in arr:
	one[i] +=1
	for i in range(n):
		if i < one[0]:
			arr[i] = 0
		elif i < one[0]+one[1]:
				arr[i] = 1
		else:
			arr[i] = 2
	print(arr) 
