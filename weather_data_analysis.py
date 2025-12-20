import numpy as np

# Temperatures for 30 days
temps = np.array([
    22, 25, 19, 38, 41, 28, 12, 5, -2, 8, 
    31, 37, 34, 39, 25, 20, 15, 9, 4, 11, 
    36, 42, 33, 29, 18, 10, 7, 2, 24, 30
])

heatwaves = temps[temps > 35]
avg_temp = temps[temps > 0]

print(heatwaves.size, "days")
print("Average temp of above freezing days:", np.mean(avg_temp))
print(np.where(temps > 10, temps, 10))