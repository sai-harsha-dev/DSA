# Insertion Sort ---> https://www.youtube.com/watch?v=i-SKeOcBwko&t=377s

# Explanation :- The idea is to consider the value other than in those in the 
#                Iteration range to be unsorted, so everytime if we find an element 
#                smaller than in the sorted value we push the sorted array element 
#                by one index.

# Complexity:-O(N^2) - i goes through n-1 Iterations
#                      j goes through n Iterations
#                      Hence :- (n-1)n = n^2+2n = n^2
#             O(1) - Inplace sorting


n = int(input())
alist=[int(i) for i in input().split()]
for i in range(n-1):
    value=alist[i+1]
    for j in range(i,-1,-1):
        if value > alist[j]:
            break
        alist[j+1]=alist[j]
        alist[j] = value
print(alist)