import numpy as np

matrix=np.random.randint(1,10,(5,3))
matrix2=np.random.randint(1,10,(3,2))
product=matrix.dot(matrix2)
print(f"Product of matrixes is:\n{product}")