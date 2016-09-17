#求曲线在给定点的切线方程, 把曲线和切线一起画出来
#f(x) = x**3, (-2, -8)
#求斜率lim(h->0)(f(-2+h) - f(-2)) / h
#= lim(h->0)((-2 + h)**3 + 8) / h
#= lim(h->0)((-2 + h) * (4 -4*h + h**2) + 8) / h
#= lim(h->0)(-8 + 8*h - 2*h**2 + 4*h - 4*h**2 + h**3 + 8) / h
#= lim(h->0)(h**3 - 6*h**2 + 12*h) / h
#= lim(h->0)(h**2 - 5*h + 12)
#= 12
#P:(-2, -8)
#slop = 12
#点斜式y = (x - px)*slop + py
#      y = 12*x + 24 - 8
#      y = 12*x + 16

def f(x):
    return x**3

def t(x):
    return 12*x + 16

x = linspace(-4, 4, 100)
y = f(x)

sx = -3.0
sy = t(sx)
ex = 0.0
ey = t(ex)

xlabel('x')
ylabel('y')
plot(x, y, 'r-', [sx, ex], [sy, ey], 'g-', [-2], [-8], '*r')
text(-2.0, -8.0, '(-2,-8)')
