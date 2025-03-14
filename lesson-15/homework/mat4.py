import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x=np.random.uniform(0,10,100)
y=np.random.uniform(0,10,100)
size=np.abs(np.random.rand(100))*100

plt.scatter(x,y,s=size,c=y,cmap='cool',marker='*')
plt.xlabel("X")
plt.ylabel("Y", rotation=0)
plt.legend()
plt.title("Scatter of 100 plots")
plt.grid(True)
plt.colorbar()
plt.show()