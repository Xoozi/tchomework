
#49. f(x, y) = x*sin(y/2) + y*sin(2x)
# 0 <= x <= 5pi, 0 <= y <= 5pi, P(3pi, 3pi)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-40, 40, 0.05)
Y = np.arange(-40, 40, 0.05)
X, Y = np.meshgrid(X, Y)
Z = X*sin(Y/2) + Y*sin(2*X)

'''等位线 f(x, y) = c
    f(3pi, 3pi) = 3pi*sin(3pi/2) + y*sin(6pi) = -3pi

    等位线方程为 x*sin(y/2) + y*sin(2*x) = -3pi

    到此为止了, 我还不知道怎么把这曲线参数化

    用wolfram把这个隐式曲线画出来了, 比较迷幻

    根据wolfram的采样范围, 重新画了曲面, 确实多看出很多东西
    这个曲面感觉在几个方向都有波
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
