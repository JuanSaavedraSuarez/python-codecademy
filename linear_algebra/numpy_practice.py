import numpy as np

v = np.array([1, 2, 3, 4, 5, 6])
print(v)

a = np.array([[1, 2], [3, 4]])
print(a)

v = np.array([-2,-2,-2,-2])
u = np.array([0,0,0,0])
w = np.array([3,3,3,3])

A = np.column_stack((v, u, w))
print(A)

print(A.shape)

print(A[0,1])
print(A[:,1])