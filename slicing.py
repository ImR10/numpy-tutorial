import numpy as np

# slicing - 

array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])

# ROW SELECTION
# array[start:end:step]
print("Row 1: ", array[0])
print("Row 4: ", array[-1])
print("First 3 rows: \n", array[0:3])
print("Rows 2-4: \n", array[1:])
print("Every 2nd row:\n", array[::2])
print("Every row reversed:\n", array[::-1])

# SLICING COLUMNS
# array[start:end:step, start:end:step]
print("Col 1: ", array[:, 0])
print("Col 4: ", array[:, -1])
print("\nCol 2-4: \n", array[:, 1::])
print("\nCol 1-3: \n", array[:, :3])
print("\nEvery 2nd Col: \n", array[:, ::2])
print("\nEvery 2nd Col after Col 1: \n", array[:, 1::2])
print("\nReverse Col Order: \n", array[:, ::-1])

# SLICE BOTH ROWS AND COLUMNS   
print("\nFirst 2 rows, first 2 cols:\n", array[:2, :2])
print("\nLast 2 rows, first 2 cols:\n", array[2:, :2])
