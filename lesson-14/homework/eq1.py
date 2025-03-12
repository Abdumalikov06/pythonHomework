import numpy as np
w=np.array([[4, 5, 6], 
 [3, -1, 1], 
 [2, 1, -2]])

y=np.array([7,4,5])
solution=np.linalg.solve(w,y)
print(solution)