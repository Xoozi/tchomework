#求曲线在给定点的切线方程, 把曲线和切线一起画出来
#f(x) = 4 - x**2  点 (-1,3)
#求斜率lim(h->0)(f(-1+h) - f(-1)) / h
#= lim(h->0)((4 - (-1+h)**2) - (4 - (-1)**2))/ h
#= lim(h->0)((4 - 1 +2*h - h**2 - 4 + 1)/h
#= lim(h->0)(2*h - h**2)/h
#= lim(h->0)(2 - h)
#= 2

def f(x):
    return 4 - x**2

x = linspace(-4, 4, 100)
y = f(x)

sx = -2.0
sy = 1.0
ex = 0.0
ey = 5.0

xlabel('x')
ylabel('y')
plot(x, y, 'r-', [sx, ex], [sy, ey], 'g-', [-1], [3], '*r')
text(-1.0, 3.0, '(-1,3)')
