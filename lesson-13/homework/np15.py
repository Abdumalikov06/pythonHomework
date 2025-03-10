import numpy as np

matrix=[[ 4 , 7, 2,  8,  1],
 [ 9,  3,  6,  5,  2],
 [ 1, 8,  4,  7,  3],
 [ 5, 2, 9,  6,  4],
 [ 7,  1,  3, 8,  5]]

row_sums = np.sum(matrix, axis=1)
print("\nRow-wise Sums:", row_sums)

col_sums = np.sum(matrix, axis=0)
print("\nColumn-wise Sums:", col_sums)