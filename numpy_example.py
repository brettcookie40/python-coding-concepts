# Numpy is a python library used for linear algebra
# Provides features for operations on multi-dimensional arrays and matrices in python

import numpy as np

a = np.array([1,2,3])

print(a)

b = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(b)

# How can you initialize a 5x5 NumPy array comprising of all zeros
c = np.zeros((5,5))

print(c)

# Let's say we have two NumPy arrays as follows:
# [1, 2, 3] and [4, 5, 6]
# How can you add the individual elements?

first = np.array([1,2,3])
second = np.array([4,5,6])

# third = first + second # non numpythonic way
print(np.sum((first,second), axis=0))

# Changing the axis to 1 will add each of the values in each respective array and
# return back those values
# print(np.sum((first,second), axis=1))