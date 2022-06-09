# Problem Description

	# Given a non-negative number represented as an array of digits, 
	# add 1 to the number ( increment the number represented by the digits ).
	# The digits are stored such that the most significant digit is at the head 
	# of the list.

	# NOTE: Certain things are intentionally left unclear in this question 
	# which you should practice asking the interviewer. For example: 
	# for this problem, following are some good questions to ask :

	# 	Q : Can the input have 0's before the most significant digit. Or in 
	# 	other words, is 0 1 2 3 a valid input?
	# 	A : For the purpose of this question, YES
	# 	Q : Can the output have 0's before the most significant digit? 
	# 	Or in other words, is 0 1 2 4 a valid output?
	# 	A : For the purpose of this question, 
	# 	NO. Even if the input has zeroes before the most significant digit.

# SOLUTION 
# 	Time complexity O(n)  
# 	Space complexity O(1)

A = [int(i) for i in input().split()]
num = 0
for i in A:
	num = num*10 + i
num += 1
num = str(num)
A = [x for x in num]
print(A)