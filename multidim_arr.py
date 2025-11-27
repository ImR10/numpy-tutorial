import numpy as np

# 0-dimension array
array = np.array('A')
print("Number of Dimensions: ", array.ndim)

# 1-dimension array
array = np.array(['A', 'B', 'C'])
print("Number of Dimensions: ", array.ndim)

# 2-dimension array
array = np.array([['A', 'B', 'C'],
                  ['D', 'E', 'F'],
                  ['G', 'H', 'I']])
print("Number of Dimensions: ", array.ndim)

# 3-dimension array
# Each list must have a consistent number of elements
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]])
print("Number of Dimensions: ", array.ndim)
print("Array shape: ", array.shape)  # (detph (layers), rows, columns)

# Multi-dimensional indexing
word = array[1, 1, 1] + array[2, 0, 2] + \
    array[1, 1, 0] + array[1, 2, 0] + array[2, 2, 0]
print(word)
