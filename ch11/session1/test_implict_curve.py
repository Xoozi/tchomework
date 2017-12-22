import matplotlib.pyplot
from numpy import arange
from numpy import meshgrid

delta = 0.025
xrange = arange(-5.0, 20.0, delta)
yrange = arange(-5.0, 20.0, delta)
X, Y = meshgrid(xrange,yrange)

# F is one side of the equation, G is the other
F = Y**X
G = X**Y

matplotlib.pyplot.contour(X, Y, (F - G), [0])
matplotlib.pyplot.show()
