import matplotlib.pyplot as plt
import numpy as np

# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)  # (rows,columns,first)
plt.plot(x, y)
plt.title("first_plot")

# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)  # (rows,columns,second)
plt.plot(x, y)
plt.title("second_plot")


plt.suptitle("SUBPLOTS")
plt.show()
