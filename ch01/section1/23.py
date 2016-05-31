
#设f(x) = sin(x)/x
#
#(a)分别从两个方向让x趋于0来估计lim(x->0)f(x)的值
#(b)用f(x) 在x0=0附近的图来说明

def f(x):
    return sin(x)/x

fl1 = f(0.1)
fl2 = f(0.01)
fl3 = f(0.001)
fl4 = f(0.0001)
fl5 = f(0.00001)

fr1 = f(-0.1)
fr2 = f(-0.01)
fr3 = f(-0.001)
fr4 = f(-0.0001)
fr5 = f(-0.00001)


print 'fl(%f, %f, %f, %f, %f) fr(%f, %f, %f, %f, %f)' % (fl1, fl2, fl3, fl4, fl5, fr1, fr2, fr3, fr4, fr5)


x1 = linspace(-1, -0.0000001, 100)
y1 = f(x1)

x2 = linspace(0.0000001, 1, 100)
y2 = f(x2)


xlabel('x')
ylabel('y')
plot(x1, y1, 'r-', x2, y2, 'g-')
