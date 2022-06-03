# Subarray with given sum

# 	Given an unsorted array A of size N that contains 
# 	only non-negative integers, find a continuous sub-array 
# 	which adds to a given number S.
# 	In case of multiple subarrays, return the subarray which comes first 
# 	on moving from left to right.

#  	Example 1:

# 	Input:
# 	N = 5, S = 12
# 	A[] = {1,2,3,7,5}
# 	Output: 2 4
# 	Explanation: The sum of elements 
# 	from 2nd position to 4th position 
# 	is 12.
 

# 	Example 2:

# 	Input:
# 	N = 10, S = 15
# 	A[] = {1,2,3,4,5,6,7,8,9,10}
# 	Output: 1 5
# 	Explanation: The sum of elements 
# 	from 1st position to 5th position
# 	is 15

# 	Sol :- O(n),O(1)
#  Video explanation :- https://www.youtube.com/watch?v=q5m1WmJmkuM
n=int(input())
arr = [int(i) for i in input().split()]
s = int(input())
output = []
left = 0
right = 0
total = arr[0]
while right < n:
	if s == total:
		output.append(left+1)
		output.append(right+1)
		print(output)
		break
	elif total < s:
		if right+1 == n:
			break
		right+=1
		total += arr[right]
			
	elif total > s:
		total-=arr[left]
		left+=1
if len(output) == 0:			
	output.append(-1)        
	print(output)

