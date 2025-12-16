import numpy as np

# Scalar Arithmetic
array = np.array([1, 2, 3])
print(array)
print(array+1)
print(array/4)
print(array ** 5)

# Vectorized Math Functions
print(np.sqrt(array))

array = np.array([1.01, 2.5, 3.99])
print(np.round(array))
# round down
print(np.floor(array))
# round up
print(np.ceil(array))
# pi
print(np.pi)

radii = np.array([1, 2, 3])
print(np.pi * radii ** 2)

# ELEMENT-WISE ARITHMETIC
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 ** array2)

# COMPARISON OPERATORS
scores = np.array([91, 55, 100, 73, 82, 64])
scores[scores < 60] = 0
print(scores)