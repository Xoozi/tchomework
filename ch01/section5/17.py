#具有指定斜率的切线
#求曲线 y = 1/(x - 1)的斜率为-1的所有切线
#f(x) = 1/(x - 1)
#求斜率lim(h->0)(f(x+h) - f(x)) / h
#= lim(h->0)(1/(x+h-1) - 1/(x-1)) / h
#= lim(h->0)((x - 1 - x - h + 1)/(x+h-1)*(x-1)) / h
#= lim(h->0)(-1/(x+h-1)*(x-1))
#= -1/(x-1)*(x-1)
#= -1/(x-1)*(x-1)
#if slop = -1
# x**2 - 2*x + 1 = 1
# x**2 - 2*x = 0
# x*(x - 2) = 0
# x = 0 or x = 2
# y = -1 or y = 1
#点斜式y = (x - px)*slop + py
#      y = (x - 0) * -1 - 1
#      y = -x - 1
#点斜式y = (x - px)*slop + py
#      y = (x - 2) * -1 + 1
#      y= -x + 3
def f(x):
    return 1/(x - 1)

def t1(x):
    return  -x - 1
def t2(x):
    return  -x + 3

x1 = linspace(-1, 0.5, 100)
y1 = f(x1)
x2 = linspace(1.5, 3, 100)
y2 = f(x2)

tx1 = 0
ty1 = f(tx1)
sx1 = -1.0
sy1 = t1(sx1)
ex1 = 0.5
ey1 = t1(ex1)

tx2 = 2
ty2 = f(tx2)
sx2 = 1.5
sy2 = t2(sx2)
ex2 = 3.0
ey2 = t2(ex2)

xlabel('x')
ylabel('y')
plot(x1, y1, 'r-', [sx1, ex1], [sy1, ey1], 'g-', [tx1], [ty1], '*r')
text(tx1, ty1, '(%.1f,%.1f)' % (tx1, ty1))

plot(x2, y2, 'r--', [sx2, ex2], [sy2, ey2], 'g--', [tx2], [ty2], '*r')
text(tx2, ty2, '(%.1f,%.1f)' % (tx2, ty2))
