#画给定区间上函数图像然后
#(a)在给定区间上积分函数
#(b)求图像和x轴之间的面积
#y = 2*x - x**2

p = poly1d([-1, 2, 0])
P = p.integ()

def f(x):
    return polyval(p, x)

def F(x):
    return polyval(P, x)

x = linspace(0, 3, 1000)
y = f(x)

a1 = F(2.0) - F(0)
a2 = F(3.0) - F(2.0)
a = a1 + a2
sa = a1 - a2

print "a1:%f, a2:%f, a:%f, sa:%f" % (a1, a2, a, sa)

plot([0, 3], [0, 0], '-k')

plot(x, y, '-r')


