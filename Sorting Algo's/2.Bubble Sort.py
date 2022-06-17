# Bubble Sort --> https://www.youtube.com/watch?v=Jdtq5uKz-w4&t=283s

# Explanation :- The idea here is to sort the array from right to left, meaning that 
#                in every iteration the highest value(maximum)is pushed to the last 
#                unsorted index to the right.

# Points to remember :- 1) Sorts right to left
#                       2) Sorts maximum value first
#                       3) Compares the adjecent index values.

# Complexity :- O(N^2) :-i goes through n-1 Iterations
#                       j goes through n-1-i Iterations
#                       Hence :- (n-1)(n-1-i) = n^2+2n+(1-i) = n^2
#               O(1) :- Inplace 

n = int(input())
arr=[int(i) for i in input().split()]
for i in range(n-1):           # n-1 since last element needs no comparision
    swap = 0                   # To trak if a swap happend in an iteration
    for j in range((n-1)-i):   # Since n-1-i element is already sorted
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            swap = 1
    if swap == 0:  # No swap happended menaing adjecent elements are already sorted
        break
print(arr)