#设f(x) = x**(1/(1-x))
#
#(a)对从x0=1两个方向趋于1的x的f(x)列表, x->1时f(x)看似有极限吗, 如果有极限, 极限值是什么, 如果没极限解释一下
#(b)用f(x) 在x0=1附近的图来说明

def f(x):
    return x**(1/(1-x))

fl1 = f(1.1)
fl2 = f(1.01)
fl3 = f(1.001)
fl4 = f(1.0001)
fl5 = f(1.00001)

fr1 = f(0.9)
fr2 = f(0.99)
fr3 = f(0.999)
fr4 = f(0.9999)
fr5 = f(0.99999)


print 'fl(%f, %f, %f, %f, %f) fr(%f, %f, %f, %f, %f)' % (fl1, fl2, fl3, fl4, fl5, fr1, fr2, fr3, fr4, fr5)


x1 = linspace(1.0000001, 2 ,100)
y1 = f(x1)

x2 = linspace(0, 0.9999999, 100)
y2 = f(x2)


xlabel('x')
ylabel('y')
plot(x1, y1, 'r-', x2, y2, 'g-')
