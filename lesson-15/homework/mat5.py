import numpy as np
import matplotlib
import matplotlib.pyplot as plt

mean=0
std=1
data=np.random.normal(0,1,1000)
plt.hist(data,bins=30,alpha=0.7,label="Dataset", color='b',edgecolor='black')
plt.xlabel("Count")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()