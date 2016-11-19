

#求由直线和曲线所围区域面积
#y = 2*sin(x), y = sin(2*x), 0 <= x <= pi


def f1(x):
    return 2*sin(x)

def f2(x):
    return sin(2*x)

def f(x):
    return 2*sin(x) - sin(2*x)

def F(x):
    return -2*cos(x) + 1/2*cos(2*x)


x = linspace(0, pi, 1000)
y1 = f1(x)
y2 = f2(x)

a = F(pi) - F(0)

print 'area=%f' % (a)


plot([0, pi], [0, 0], '-k')

plot(x, y1, '-r', x, y2, '-g')


