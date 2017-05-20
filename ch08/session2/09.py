#Newton方法
#下列序列来自Newton方法的递推公式, 序列是否收敛? 如果收敛, 收敛到什么值?

def sec(x):
    return 1.0/cos(x)

#(a) x0 = 1, xn+1 = xn - (xn² - 2)/2xn = xn/2 + 1/xn
def ra(xn):
    return xn/2.0 + 1.0/xn

#(b) x0 = 1, xn+1 = xn - (tanxn - 1)/sec²xn
def rb(xn):
    return xn - (tan(xn) - 1.0)/(sec(xn)**2)

#(c) x0 = 1, xn+1 = xn - 1
def rc(xn):
    return xn - 1.0

def newton(rfun, x0):
    xp = x0
    xn = 0.0

    delta = xn - xp
    cnt = 0

    while cnt < 100 and (delta > 0.0000001 or delta < -0.0000001) :
        xn = rfun(xp)
        delta = xn - xp
        xp = xn
        cnt = cnt + 1

    print 'fun:%s, cnt:%d, xn:%f, delta:%f' % (rfun.__name__, cnt, xn, delta)

newton(ra, 1.0);
newton(rb, 1.0);
newton(rc, 1.0);
