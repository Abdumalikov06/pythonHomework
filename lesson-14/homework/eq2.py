import numpy as np

w=np.array([
    [10,-2,3],
    [-2,8,-1],
    [3,-1,6]
    ])
y=np.array([12,-5,15])

solution=np.round(np.linalg.solve(w,y),3)
print(f'l1 is {solution[0]}')
print(f'l2 is {solution[1]}')
print(f'l3 is {solution[2]}')