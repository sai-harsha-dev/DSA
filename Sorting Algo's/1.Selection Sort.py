# Selection Sort --> https://www.youtube.com/watch?v=GUDLRan2DWM 

# Explanation:-The idea is to start sorting from from starting index and move over to 
#              the next index so,in every iteration left part of the array gets sorted

# Complexity:-O(N^2) - i goes through n-1 Iterations
#                      j goes through n-1 Iterations
#                      Hence :- (n-1)(n-1) = n^2+2n+1 = n^2
#             O(1) - Inplace sorting

n = int(input())
arr=[int(i) for i in input().split()]
for i in range(n-1):            # n-1 since last element needs no comparision
    for j in range(i,n):
        if arr[i] > arr[j]:
            temp = arr[i] 
            arr[i] = arr[j]
            arr[j] = temp
print(arr)