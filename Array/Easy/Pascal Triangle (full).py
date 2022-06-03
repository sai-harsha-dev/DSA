
# 2)  PASCALS TRIANGLE ( Generate whole triangle )

#     * PROBLEM STATEMENT *

#         Given numRows, generate the first numRows of Pascal's triangle.
#         Pascal's triangle : To generate A[C] in row R, 
#         sum up A'[C] and A'[C-1] from previous row R - 1.

#         Example:

#         Given numRows = 5,

#         Return

#         [
#              [1],
#              [1,1],
#              [1,2,1],
#              [1,3,3,1],
#              [1,4,6,4,1]
#         ]

#     SOL1)
#     •	TC – O(N**2) 
#     •	SC – O(N)
    
A =int(input())   
op = [1]
output = []
for i in range(A):
    for j in range(i+1):
        if j==0 or j == i:
            op.append(1)
        else:
            op.append(op[len(op)-(i+1)] + op[len(op)-i])
    output.append(op[len(op)-(i+1):])
print(output)
