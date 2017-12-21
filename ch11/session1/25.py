

#25. f(x, y) = 4x**2 + y**2

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
Z = 4*X**2 + Y**2

#等位线 f(x, y) = c
#4*x**2 + y**2 = 2
#x**2/(1/2) + y**2/2 = 1
#
#4*x**2 + y**2 = 4
#x**2/1 + y**2/4 = 1
#
#4*x**2 + y**2 = 8
#x**2/2 + y**2/8 = 1
t = linspace(0, 2*pi, 1000)
x = 0.5*cos(t)
y = 2*sin(t)
z = 0*t
ax.plot(x, y, z, '-r')
x = 1*cos(t)
y = 4*sin(t)
ax.plot(x, y, z, '-g')
x = 2*cos(t)
y = 8*sin(t)
ax.plot(x, y, z, '-b')


# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)

# Customize the z axis.
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
