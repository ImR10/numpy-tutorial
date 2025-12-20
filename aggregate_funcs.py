import numpy as np

# aggregate functions summarize data and typically return a single value

array = np.array([[1,2,3,4,5],
                   [6,7,8,9,10]])

print("Sum:", np.sum(array))
print("Mean:", np.mean(array))
print("Spread:", np.std(array))
print("Variance:", np.var(array))
print("Min value:", np.min(array))
print("Max value:", np.max(array))
print("Min value position:", np.argmin(array))
print("Max value position:", np.argmax(array))
print("Sum each column:", np.sum(array, axis=0))
print("Sum each row:", np.sum(array, axis=1))
