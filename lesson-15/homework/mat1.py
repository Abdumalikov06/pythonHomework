import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x=np.linspace(-10,10, 1000)

def f_x(x):
    return  x**2 - 4*x + 4

y=f_x(x)

plt.plot(x,y, label= "$x^2 - 4x + 4$")
plt.xlabel("X")
plt.ylabel("Y", rotation=0)
plt.legend()
plt.show()
