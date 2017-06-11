#∑(n=1, ∞) (-1)**n 1/(2n)!, 以大小1小于5*10**(-6)的误差逼近级数的和
#
#       根据交错级数截断误差估计定理
#       n项和的截断误差小于an+1
#       也就是要找一个an+1<5*10**(-6)

def an(n):
    return 1.0/math.factorial(2*n);

a = an(1)
s = 0
e = 0.000005
n = 1

while(a > e):
    s += a
    n += 1
    a = an(n)

print 'n:%d, sum:%f' % (n-1, s)

#结论是4
