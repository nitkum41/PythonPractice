import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 50, 10, 70])
ypoints = np.array([0, 40, 50, 250])

# plt.plot( ypoints)
# plt.plot(xpoints, ypoints, 'o')
# plt.plot(xpoints, ypoints, ls=':')
plt.plot(xpoints, ypoints, ls='--', c='r' , lw='5')
# plt.plot(xpoints)
# plt.plot(ypoints)
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.xlabel("x-axis",fontdict=font1)
plt.ylabel("y-axis",fontdict=font2)
plt.title('LINE PLOT')

plt.grid()
plt.show()
