# Given an array of N integers, and an integer K, 
# find the number of pairs of elements in the array whose sum is equal to K.


# Example 1:

# Input:
# N = 4, K = 6
# arr[] = {1, 5, 7, 1}
# Output: 2
# Explanation: 
# arr[0] + arr[1] = 1 + 5 = 6 
# and arr[1] + arr[3] = 5 + 1 = 6.

# Example 2:

# Input:
# N = 4, K = 2
# arr[] = {1, 1, 1, 1}
# Output: 6
# Explanation: 
# Each 1 will produce sum 2 with any 1.

# Solution :- O(N),O(N) ---> https://www.youtube.com/watch?v=5L9Jrehvoew

# Explanation :- 1) Since K = e1+e2, we can find pairs with sum k by checking
#                   how many time k-e1 has appeared in the array. [Note*:- while
#                   doing so we must avoid counting dublicates].
#                2) To avoide counting duplicates we track the number times any 
#                   and element has appeared before the present index element

n,k = map(int,input().split())
arr = [int(i) for i in input().split()]
freq = {} # Keeps track of number of times the element appeared before
count =0  # Counts the number of pairs with sum.
for i in arr:
    diff = k-i  # finds difference 
    if diff in freq: # checks if difference has appeared before the element
        count+=freq[diff] # since no.of times diff appeared before = no.of pairs
    if i in freq:
        freq[i]+=1 # Keeps track of number of times the element appeared before
        continue
    freq[i]=1
print(count)