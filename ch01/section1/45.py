#列表法估计极限lim(x->0)f(x)
#43 f(x) = (10**x - 1)/x
def f(x):
    return (10**x - 1)/x
xl1 = -0.1
xl2 = -0.01
xl3 = -0.001
xl4 = -0.0001

xr1 = 0.1
xr2 = 0.01
xr3 = 0.001
xr4 = 0.0001

yl1 = f(xl1)
yl2 = f(xl2)
yl3 = f(xl3)
yl4 = f(xl4)

yr1 = f(xr1)
yr2 = f(xr2)
yr3 = f(xr3)
yr4 = f(xr4)

print "yl:[%f %f %f %f] yr:[%f %f %f %f]" % (yl1, yl2, yl3, yl4, yr1, yr2, yr3, yr4)
