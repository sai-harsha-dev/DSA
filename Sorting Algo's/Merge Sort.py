#MergeSort ----> https://www.youtube.com/watch?v=TzeBrDU-JaY&t=834s

#Explanation :- The idea is to break down the array into smaller halves and sort
#               and combine and create and sorted array from smaller subarray.
        
#Points to remember :- 1) Uses divide and conqour (recurssion)
#                      2) Picks random elements and finds its position in sorted array
#                      3) Needs additional memory not inplace since splitting and 
#                         creating sorted subset need additional space.
            
#Complexity :- O(nlogn) :- logn for splitting
#                          n for comparing and merging Values
#              O(N) :- to store the sorted array

from math import ceil

def sort(left,right):   # To compare subarray value and combine in sorted fashion
    l = 0     # To track used indexs in left subarray
    r = 0     # To track used indexs in right subarray 
    out=[]    # Sorted array
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            out.append(left[l])
            l += 1
            continue
        if right[r] < left[l]:
            out.append(right[r])
            r += 1
            continue
        if right[r] == left[l]:
            out.append(right[r])
            out.append(left[l])
            l+=1
            r+=1
            continue
    while l < len(left):
        out.append(left[l])
        l+=1
    while r < len(right):
        out.append(right[r])
        r+=1
    return out

def mergesort(arr):     # To create smaller subarray
    mid = len(arr)  # since mid indicates the len of array in start of each call
    if mid == 1:    # Since only one element in array returns
        return arr
    mid = ceil(mid//2) 
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return sort(left,right)

arr = [int(i) for i in input().split()]
print(mergesort(arr))