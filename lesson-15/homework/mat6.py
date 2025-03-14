import numpy as np
import matplotlib
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(8,6))
x=np.linspace(-5,5,100)
ax=plt.axes(projection='3d')
y=np.linspace(-5,5,100)
xx,yy=np.meshgrid(x,y)
zz=np.cos(pow(xx,2)+pow(yy,2))

ax.plot_surface(xx,yy,zz, cmap='viridis')
plt.title(" 3D Surface plot of $ f(x, y) = \cos(x^2 + y^2) $ ")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("z-axis",rotation=360)
plt.show()