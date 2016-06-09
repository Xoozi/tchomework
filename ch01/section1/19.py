#设f(x) = (x**2 - 9)/(x + 3)
#
#(a)对点x = -3.1, -3.01, -3.001等处的f值列表, 估算lim(x->-3)f(x), 如果能代之以f在x = -2.9, -2.99, -2.999#处的值, 又能估算得到什么

#(b)用f(x) 在x0=-3附近的图来说明

#(c)代数地求lim(x->-3)f(x)
#f(x) = ((x+3)*(x-3))/(x+3) = x-3  x!=-3 所以
#                                           lim(x->-3)f(x) = -6

def f(x):
    return (x**2 - 9) / (x + 3)

fl1 = f(-3.1)
fl2 = f(-3.01)
fl3 = f(-3.001)
fl4 = f(-3.0001)
fl5 = f(-3.00001)

fr1 = f(-2.9)
fr2 = f(-2.99)
fr3 = f(-2.999)
fr4 = f(-2.9999)
fr5 = f(-2.99999)

print 'fl(%f, %f, %f, %f, %f) fr(%f, %f, %f, %f, %f)' % (fl1, fl2, fl3, fl4, fl5, fr1, fr2, fr3, fr4, fr5)


x1 = linspace(-4, -3.0000001, 100)
y1 = f(x1)

x2 = linspace(-2.9999999, -2, 100)
y2 = f(x2)


xlabel('x')
ylabel('y')
plot(x1, y1, 'r-', x2, y2, 'g-')