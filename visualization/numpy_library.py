# Library for array management
import numpy as np

a1 = np.array([2,1,3,4,5,8])
print("a1 =", a1)
a2 = np.array([[1,2,3],[2,1,2],[1,2,3]])
print("a2 =", a2)

a3 = np.arange(10, 50, 10)
print("a3 =", a3)
a4 = np.arange(15)
print("a4 =", a4)
a5 = np.arange(0.3, 2, 0.2)
print("a5 =", a5)

a6 = np.linspace(3, 8, 9) #start, stop, steps between start and stop
print("a6 =", a6)

o1 = np.ones((2,2))
print("o1 =", o1)

o2 = np.zeros((2,2))
print("o2 =", o2)

o3 = np.empty((3,4))
print("o3 =", o3)

o4 = np.eye(5)
print("o4 =", o4)

o5 = np.random.random((5,5))
print("o5 =", o5)


# BUILT IN PROCEDURES
print("a2 dimensions", a2.ndim)  # Dimensions
print("a2 shape", a2.shape)  # Format
print("a2 type", a2.dtype)  # Type of the array
print("a2 size of each item in bytes", a2.itemsize)
print("a1 ", a1.reshape(2,3))  # Reshape an array

#Replacement
c1 = np.arange(15)
b1 = c1 > 9 # tells if all values are > than 9
print(b1)

c1[b1] = 1 # replace values with a True in the True/false map
print(c1)


c2 = np.arange(25).reshape(5,5) # 5 * 5 matrix
print(c2.max()) # Max value of the matrix
print(c2.max(axis=0)) # Max value of the column
print(c2.max(axis=1)) # Max value of the row

print(c2.min()) # Min value of the matrix
print(c2.sum()) # Sum value of the matrix
print(c2.cumsum())

# Copy
c3 = c2.copy()
c3[0,0] = 16
print(c2)

# Stacking arrays
v1 = np.array([2,1,3,4])
v2 = np.array([5,1,7,6])
print(np.vstack((v1,v2)))
print(np.hstack((v1,v2)))


# Operations
x = np.linspace(0, 6.28, 20)
print(np.sin(x)) #calculate sin of every elements
x1 = np.arange(9).reshape(3,3)
print(x > 4) # returns a new array with the result of the operation
print( x ** 2) # returns a new array with the result of the operation

