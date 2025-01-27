import numpy as np
a = np.arange(10,22).reshape((3, 4))  ##2d arra of 3 rows 4 columns
print("Original array:")
print(a)
print("Each element of the array is:")
for x in np.nditer(a):
  print(x,end=None)