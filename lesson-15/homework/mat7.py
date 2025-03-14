import numpy as np
import matplotlib
import matplotlib.pyplot as plt

data1=['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
data2=[200, 150, 250, 175, 225]
colors = ['red', 'blue', 'green', 'purple', 'orange']
plt.bar(data1,data2,width=0.8, color=colors, edgecolor='black')
plt.title("Sales data for 5 different countries")
plt.xlabel('Countries')
plt.ylabel("Values")
plt.show()