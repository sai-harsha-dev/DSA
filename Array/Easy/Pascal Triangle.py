# 1)  PASCALS TRIANGLE ( Generate specific row )
#     https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/

    # SOL1)
    # •	TC – O(N**2) 
    # •	SC – O(N)
A =int(input())
op = []
for i in range(A+1):                                      # To generate each row
    for j in range(i+1):                                  # To generate elements in each row
        if j == 0 or j == i:                              # First and last element is always 1
            op.append(1)
        else:                                             
            op.append(op[len(op)-i] + op[len(op)-(i+1)])  # Generates in between elements by summing up elements of previous row
print(op[(len(op)-A)-1:])

    # SOL2)
    # •	TC – O(N) 
    # •	SC – O(N)
     
    #  Refer youtube link ---->   https://www.youtube.com/watch?v=F5weB2hg-8Q