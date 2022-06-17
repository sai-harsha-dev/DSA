# Insertion Sort ---> https://www.youtube.com/watch?v=i-SKeOcBwko&t=377s

# Explanation :-The idea is to consider a part of an array till an index(initially 1)
#               as being sorted, and then picking the next element to the right and
#               find out its position in the sorted portion and insert it into that
#               particular index and extend the sorted array by one index.

# Points to remember :- 1) Sorts right to left
#                       2) Picks and value and finds it position in sorted array.
#                       3) Compares the i+1 index value eith value before it.

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