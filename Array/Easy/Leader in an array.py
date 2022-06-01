# Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 

#  	Example 1:
# 	Input:
# 	n = 6
# 	A[] = {16,17,4,3,5,2}

# 	Output: 17 5 2
# 	Explanation: The first leader is 17 as it is greater than all the elements to its right.  
# 	Similarly, the next leader is 5. The right most element is always a leader so it is also included.
 
# 	Example 2:
# 	Input:
# 	n = 5
# 	A[] = {1,2,3,4,0}

# 	Output: 4 0

# 	Sol :- O(n),O(n)

A =[int(i) for i in input().split()]
N = len(A)
count = []
compare = [i for i in A]
for i in range(N-1,0,-1):
    if A[i] > A[i-1]:
        A[i-1] =  A[i]
for i in range(N-1):
        if compare[i] >= A[i+1]:	
            count.append(compare[i])
count.append(compare[N-1])
print(count)