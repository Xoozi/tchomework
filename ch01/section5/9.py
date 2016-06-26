#求曲线在给定点的切线方程, 把曲线和切线一起画出来
#f(x) = x - 2*x**2, (1, -1)
#求斜率lim(h->0)(f(1+h) - f(1)) / h
#= lim(h->0)((1+h) - 2*(1+h)**2 + 1)/ h
#= lim(h->0)(1 + h - 2 - 4*h - 2*h**2 + 1) / h
#= lim(h->0)(-2*h**2 - 3*h)/h
#= lim(h->0)(-2*h - 3)
#= -3
#P:(1, -1)
#slop = -3
#点斜式y = (x - px)*slop + py
#      y = (x - 1) * -3 - 1
#      y = -3*x + 2

def f(x):
    return x - 2*x**2

def t(x):
    return -3*x + 2

x = linspace(-4, 4, 100)
y = f(x)

tx = 1.0
ty = -1.0
sx = 0.0
sy = t(sx)
ex = 2.0
ey = t(ex)

xlabel('x')
ylabel('y')
plot(x, y, 'r-', [sx, ex], [sy, ey], 'g-', [tx], [ty], '*r')
text(tx, ty, '(%f,%f)' % (tx, ty))
