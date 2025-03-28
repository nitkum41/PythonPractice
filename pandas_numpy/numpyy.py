import numpy as np

from numpy import std

arr = np.array([[5, 2, 7, 4], [9, 6, 17, 8]])

print(type(arr[0]))

print(np.sort(arr[0]))
print(len(arr))
print(std(arr[0][1:3]))

