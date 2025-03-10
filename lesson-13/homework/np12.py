import numpy as np

a=np.random.randint(1,10,(3,4))
b=np.random.randint(1,10,(4,3))
b.reshape(3,4)
prod=a.dot(b)
print(f"First matrix:\n{a}")
print(f"Second matrix:\n{b}")

print("Product of the given matrixes:\n",prod)