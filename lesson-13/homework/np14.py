import numpy as np

# Define a 3x3 matrix A
A = np.array([[2, 3, 1], 
              [4, 1, 5], 
              [6, 2, 3]])

# Define a 3x1 column vector b
b = np.array([[5], 
              [10], 
              [8]])

# Solve for x using np.linalg.solve()
x = np.linalg.solve(A, b)

print("Solution (x):\n", x)
