import numpy as np

matrix=np.random.randint(1,101,(5,5))
mat_min=matrix.min()
mat_max=matrix.max()
normalized=(matrix-mat_min)/(mat_max-mat_min)
print(f"Normalized matrix:\n{normalized}")