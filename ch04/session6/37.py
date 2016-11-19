
#求由直线和曲线所围区域面积
#y = sin(pi/2*x), y = x


def f1(x):
    return sin(x*pi/2)

def f2(x):
    return x

def f(x):
    return sin(x*pi/2) - x

def ff(x):
    return sin(x*pi/2) - 3*x

def F(x):
    return -2.0/pi*cos(x*pi/2.0) - 1.0/2.0 * x**2



x = linspace(0, pi, 1000)
y1 = f1(x)
y2 = f2(x)
y = f(x)
yy=ff(x)

a = F(1) - F(0)

print 'area=%f' % (a)


plot([0, pi], [0, 0], '-k')

plot(x, y1, '-r', x, y2, '-g', x, y, '-b', x, yy, '^b')


