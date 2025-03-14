import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x=np.linspace(-1,(2/np.pi),10000)

def f_x(x):
    return np.sin(x)
def g_x(x):
    return np.cos(x)

y1=f_x(x)
y2=g_x(x)

plt.plot(x,y1,label="$cosx$",color='blue',marker='.')
plt.plot(x,y2, label="$sinx$", linestyle="dashed",color='red',marker='*')
plt.xlabel("x")
plt.ylabel("Y",rotation=0)
plt.legend()
plt.show()