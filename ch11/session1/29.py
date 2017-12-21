

#29. f(x, y) = 16 - x**2 - y**2
#求过(2*sqrt(2), sqrt(2))的等位线方程
#f(sqrt(8), sqrt(2)) = 6
#等位线为16 - x**2 - y**2 = 6
#x**2 + y**2 = 10

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-10, 10, 0.2)
Y = np.arange(-10, 10, 0.2)
X, Y = np.meshgrid(X, Y)
Z = 16 - X**2 - Y**2

#等位线 f(x, y) = c
t = linspace(0, 2*pi, 1000)
x = sqrt(10)*cos(t)
y = sqrt(10)*sin(t)
z = 0*t
ax.plot(x, y, z, '-r')


# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)

# Customize the z axis.
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
