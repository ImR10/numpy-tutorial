import numpy as np

# Filtering = selecting elements that match a specific condition

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

teens = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[(ages >= 65)]

print("Teens:", teens)
print("Adults:", adults)
print("Seniors:", seniors)

# np.where(condition, array, replacement)
adults = np.where(ages >= 18, ages, 0)
print(adults)