

#51. f(x, y) = sin(x + 2 cos(y))
# -2pi <= x <= 2pi, -2pi <= y <= 2pi, P(pi, pi)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
TWO_PI = 2*pi
X = np.arange(-TWO_PI, TWO_PI, 0.05)
Y = np.arange(-TWO_PI, TWO_PI, 0.05)
X, Y = np.meshgrid(X, Y)
Z = sin(X + 2*cos(Y))

'''等位线 f(x, y) = c
    f(pi, pi) = sin(pi + 2)

    等位线方程为 sin(x + 2*cos(y) = sin(pi + 2)

    到此为止了, 我还不知道怎么把这曲线参数化

    用wolfram把这个隐式曲线画出来了
'''



# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)

# Customize the z axis.
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
