import numpy as np

arr=np.array([32, 68, 100, 212, 77])


def to_cel(f):
    """Converts Fahrenhit to celcius"""
    return (f-32)*(5/9)

vectorized=np.vectorize(to_cel)


print(vectorized(arr))