import numpy as np

# 4x4 id matrix
id = np.eye(4)

print(id)

# zeros matrix
z = np.zeros((5,3))
print(z)

a = np.array([[1,2],[3,4]])
a_trans = a.T
print(a)
print(a_trans)

######################################################################################################################################

# Given
A = np.array([[1,-1,1], [0,1,0], [-1,2,1]])
B = np.array([[0.5,1.5,-0.5], [0,1,0], [0.5,-0.5,0.5]])

print(np.matmul(A,B))
print(np.matmul(B,A))

print(A.T)
print(B.T)