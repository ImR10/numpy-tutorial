import numpy as np

# 0-dim array 
array = np.array('A')
print(array.ndim)

# 1-dim array
array = np.array(['A', 'B', 'C'])
print(array.ndim)

# 2-dim array
array = np.array([['A', 'B', 'C'], 
                  ['D', 'E', 'F'], 
                  ['G', 'H', 'I']])
print(array.ndim)

# 3-dim array
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']], 
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]])
print(array.ndim)

# shape - returns tuple of (# of depth, # of rows, # of cols)
print(array.shape)

# Chain indexing - retrive element from array
print(array[0][0][0])

# Multidimensional indexing - 
print(array[0, 0, 0])

word = array[1,2,2] + array[0, 2, 2] + array[2,2,1] + array[2,1,1] + array[0,0,0] + array[1,1,1]
print(word)