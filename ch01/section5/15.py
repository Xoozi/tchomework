#具有指定斜率的切线
#求哪些位置有水平切线
#f(x) = x**2 + 4*x - 1
#求斜率lim(h->0)(f(x+h) - f(x)) / h
#= lim(h->0)(x**2 + 2*x*h + h**2 + 4*(x+h) - 1 - x**2 - 4*x + 1) / h
#= lim(h->0)(2*x*h + h**2 + 4*x + 4*h -4*x) / h
#= lim(h->0)(2*x*h + h**2 + 4*h)/h
#= lim(h->0)(2*x + h + 4)
#= 2*x + 4
#P:(-2, -5)
#slop = 0
#x = -2
#点斜式y = (x - px)*slop + py
#      y = (x - -2) * -0 + -5
#      y = -5
def f(x):
    return x**2 + 4*x - 1

def t(x):
    return  -5

x = linspace(-4, 0, 100)
y = f(x)

tx = -2.0
ty = f(tx)
sx = -4
sy = t(sx)
ex = 0
ey = t(ex)

xlabel('x')
ylabel('y')
plot(x, y, 'r-', [sx, ex], [sy, ey], 'g-', [tx], [ty], '*r')
text(tx, ty, '(%.1f,%.1f)' % (tx, ty))
