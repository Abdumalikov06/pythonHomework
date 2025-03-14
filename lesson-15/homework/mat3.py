import numpy as np
import matplotlib 
import matplotlib.pyplot as plt


x=np.linspace(-2,2,1000)
x_log = np.linspace(0.01, 2, 1000)
def f_x(x):
    return x**3
def sin_x(x):
    return np.sin(x)
def e_x(x):
    return np.exp(x)
def log(x):
    return np.log(x-1)

y1=f_x(x)
y2=sin_x(x)
y3=e_x(x)
y4=log(x_log)

fig,axs=plt.subplots(2,2,figsize=(10,8))
axs[0, 0].plot(x, y1, 'b', label=r'$f(x) = x^3$')
axs[0, 0].set_title(r'$f(x) = x^3$')
axs[0, 0].legend()
plt.xlabel("X")
plt.ylabel('Y',rotation=0)

axs[0, 1].plot(x, y2, 'r', label=r'$f(x) = \sin(x)$')
axs[0, 1].set_title(r'$f(x) = \sin(x)$')
axs[0, 1].legend()
plt.xlabel("X")
plt.ylabel('Y',rotation=0)

axs[1, 0].plot(x, y3, 'g', label=r'$f(x) = e^x$')
axs[1, 0].set_title(r'$f(x) = e^x$')
axs[1, 0].legend()
plt.xlabel("X")
plt.ylabel('Y',rotation=0)

axs[1, 1].plot(x_log, y4, 'k', label=r'$f(x) = \log(x+1)$ (for $x \geq 0$)')
axs[1, 1].set_title(r'$f(x) = \log(x+1)$')
axs[1, 1].legend()
plt.xlabel("X")
plt.ylabel("Y", rotation=0)
plt.legend()
plt.tight_layout()
plt.show()
