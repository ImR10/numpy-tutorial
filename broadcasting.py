import numpy as np

# BROADCASTING
# Allows NumPy to perform operations on array s with 
# different shaped by virtually expanding dimensions 
# so the match with larger array's shape. 

# 2 RULES: 
# 1. Dimensions have same size 
# 2. One of the dimensions has a size of 1

array1 = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12], 
                   [13, 14, 15, 16]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)

array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array2 = np.array([[1], [2], [3] ,[4] ,[5] ,[6] ,[7] ,[8] ,[9] ,[10]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)