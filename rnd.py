import numpy as np

rng = np.random.default_rng()
# seed makes copy of same results
rng_seed = np.random.default_rng(seed=1)

# rng.integer(inclusive, exclusive)
print("No seed:", rng.integers(low=1, high=101, size=(3, 2)))
print("\nWith seed:",rng_seed.integers(low=1, high=101, size=(3, 2)))

# FLOATING POINT NUMBERS
print(np.random.uniform())# prints random number b/w 0 and 1

print(np.random.uniform(low = -1, high = 1, size=[3,2]))

# shuffle array
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])
fruits = rng.choice(fruits, size = (2,5)) # picks only 'size' object(s) from array
print(fruits)