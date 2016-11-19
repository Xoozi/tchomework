#求由直线和曲线所围区域面积
#y = x**2 - 2, y = 2

pc = poly1d([1, 0, -2])
pl = poly1d([2])
p = pl-pc
P = p.integ()

def fC(x):
    return polyval(pc, x)

def fL(x):
    return polyval(pl, x)

def f(x):
    return polyval(p, x)

def F(x):
    return polyval(P, x)

x = linspace(-3, 3, 1000)
y = f(x)
yc = fC(x)
yl = fL(x)

a= F(2) - F(-2)

print 'area is:%f' % (a)



plot([-3, 3], [0, 0], '-k')

plot(x, y, '-r', x, yc, '-g', x, yl, '-b')


