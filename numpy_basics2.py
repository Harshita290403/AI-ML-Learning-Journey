# Question 2: Given a 3×3 matrix:
#  - Find its transpose.    
# - Find the sum of each row and each column.
import numpy as np
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
# transpose
transpose = matrix.T
print(transpose)

# sum of each row and column
row_sum = np.sum(matrix, axis=1)
print(row_sum)

column_sum = np.sum(matrix, axis=0)
print(column_sum)

# output:
# trannspose- 

# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]

# row sum:
# [ 6 15 24 ]

# column sum:
# [12 15 18]