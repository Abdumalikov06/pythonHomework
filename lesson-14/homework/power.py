import numpy as np

def custom(num,pow):
    """function to return given numbers power"""
    return num**pow

vectorized=np.vectorize(custom)

arr1=np.array([2, 3, 4, 5])
arr2=np.array([1, 2, 3, 4])

print(vectorized(arr1,arr2))