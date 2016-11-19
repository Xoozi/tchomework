#求第一象限中由直线y = x, 直线x = 2, 曲线y = 1/x**2和x轴所界定区域的面积


def fl(x):
    return x

def fc(x):
    return 1/x**2

def F1(x):
    return 1.0/2.0 * x**2

def F2(x):
    return -1.0/x

a = F1(1) - F1(0) + F2(2) - F2(1)

print 'area=%f' % (a)


x = linspace(0.5, 2, 1000)
y1 = fl(x)
y2 = fc(x)
plot([0, 3], [0, 0], '-k', [2, 2], [-2, 2], '-k')

plot(x, y1, '-r', x, y2, '-g')


