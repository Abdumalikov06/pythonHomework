import numpy as np
import matplotlib.pyplot as plt

time_periods = ['T1', 'T2', 'T3', 'T4']

category_A = [10, 15, 20, 25]  
category_B = [5, 10, 15, 10]   
category_C = [8, 12, 10, 15]   
plt.figure(figsize=(7, 5))
plt.bar(time_periods, category_A, label='Category A', color='blue')
plt.bar(time_periods, category_B, bottom=category_A, label='Category B', color='orange')
plt.bar(time_periods, category_C, bottom=np.array(category_A) + np.array(category_B), label='Category C', color='green')
plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.title("Stacked Bar Chart Showing Category Contributions Over Time")
plt.legend()
plt.show()
