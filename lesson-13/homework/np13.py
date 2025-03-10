import numpy as np

matrix = np.random.randint(1, 10, (3, 3))  
print("Matrix (3x3):\n", matrix)

vector = np.random.randint(1, 10, (3, 1))
print("\nColumn Vector (3x1):\n", vector)
result = np.dot(matrix, vector)  
print("\nMatrix-Vector Product (3x1):\n", result)