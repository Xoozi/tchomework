
#求曲线在给定点的切线方程, 把曲线和切线一起画出来
#f(x) = x / (x - 2), (3, 3)
#求斜率lim(h->0)(f(3+h) - f(3)) / h
#= lim(h->0)((3 + h)/(3 + h - 2) - 3/(3-2)) /h
#= lim(h->0)((3 + h) / (1 + h) - 3) / h
#= lim(h->0)((3 + h - 3*(1 + h))/(1 + h)) / h
#= lim(h->0)((3 + h - 3 - 3h))/(1 + h)) / h
#= lim(h->0)((-2*h))/(1 + h)) / h
#P:(3, 3)
#slop = -2
#点斜式y = (x - px)*slop + py
#      y = (x - 3) * -2 + 3
#      y = -2*x + 6 + 3
#      y = -2*x + 9
def f(x):
    return x / (x - 2)

def t(x):
    return -2*x + 9

x = linspace(2.1, 3.1, 100)
y = f(x)

tx = 3.0
ty = 3.0
sx = 2.1
sy = t(sx)
ex = 3.1
ey = t(ex)

xlabel('x')
ylabel('y')
plot(x, y, 'r-', [sx, ex], [sy, ey], 'g-', [tx], [ty], '*r')
text(tx, ty, '(%f,%f)' % (tx, ty))
