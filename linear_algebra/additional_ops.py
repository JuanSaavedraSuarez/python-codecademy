import numpy as np

# magnitude of vector
v = np.array([2,-4,1])
v_norm = np.linalg.norm(v)
print(v_norm)

# inverse square matrix
A = np.array([[1,2],[3,4]])
print(np.linalg.inv(A))

# solve for unknown
# each array in A is an equation from the above system of equations
A = np.array([[1,4,-1],[-1,-3,2],[2,-1,-2]])
# the solution to each equation
b = np.array([-1,2,-2])
# solve for x, y, and z
x,y,z = np.linalg.solve(A,b)

#####################################################################################################################################

# Represent the following system in NumPy matrix/vector form, then solve for x, y, and z

# Given
'''
4x + z = 2
-y + 2z - 3x = 0
.5y - x - 1.5z = -4
'''

A = np.array([[4,0,1],[-3,-1,2],[-1,.5,-1.5]])

b = np.array([2,0,-4])

x,y,z = np.linalg.solve(A,b)
print((x,y,z))