求曲线在给定点的切线方程, 把曲线和切线一起画出来
#f(x) = 1 / (x - 1), (3, 1/2)
#求斜率lim(h->0)(f(3+h) - f(3)) / h
#= lim(h->0)(1 /(3 + h - 1) - 1/2) /h
#= lim(h->0)(-h/(4 + 2h)) / h
#= lim(h->0)(-1/(4 + 2h))
#= -1/4
#P:(3, 1/2)
#slop =-1/4
#点斜式y = (x - px)*slop + py
#      y = (x - 3) * -1/4 + 1/2
#      y = -1/4*x + 3/4 + 2/4
#      y = -1/4*x + 5/4
def f(x):
    return 1/ (x - 1)

def t(x):
    return  -0.25*x + 1.25

x = linspace(1.1, 4.1, 100)
y = f(x)

tx = 3.0
ty = f(tx)
sx = 2
sy = t(sx)
ex = 4
ey = t(ex)

xlabel('x')
ylabel('y')
plot(x, y, 'r-', [sx, ex], [sy, ey], 'g-', [tx], [ty], '*r')
text(tx, ty, '(%.1f,%.1f)' % (tx, ty))
