#求由直线和曲线所围区域面积
#y = x**2, y = -x**2 + 4*x

p1 = poly1d([1, 0, 0])
p2 = poly1d([-1, 4, 0])
p = p2-p1
P = p.integ()

def f1(x):
    return polyval(p1, x)

def f2(x):
    return polyval(p2, x)

def f(x):
    return polyval(p, x)

def F(x):
    return polyval(P, x)

x = linspace(-3, 3, 1000)
y = f(x)
y1 = f1(x)
y2 = f2(x)

r = roots(p)

a= F(r[0]) - F(r[1])

print 'area is:%f' % (a)



plot([-3, 3], [0, 0], '-k')

plot(x, y1, '-r', x, y2, '-g', x, y, '-b')


