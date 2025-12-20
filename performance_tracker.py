import numpy as np

sales = np.array([
    [500, 600, 450, 700, 800, 950, 1100], 
    [300, 400, 350, 400, 500, 600, 750],  
    [900, 850, 900, 1000, 1100, 1200, 1500]
]) 

dow = np.array(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])

print("Total Sales:", np.sum(sales, axis=1))
print("Daily Trends:", np.sum(sales, axis=0)) 
low = np.argmin(sales[-1])
print("\"Sad\" Stat:", dow[low])