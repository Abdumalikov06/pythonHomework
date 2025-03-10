import numpy as np

mat1=np.random.randint(1,10,(3,3))
mat2=np.random.randint(1,10,(3,3))
product=mat1.dot(mat2)

print("THe product of 3 to 3 matrices:\n",product)