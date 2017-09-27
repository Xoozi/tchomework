#等射程发射角
#两个多大的仰角, 使抛射体到达水平距离为16千米的跟枪有同样高度的目标?
#假定初速率为400米/秒


def deg2Radian(d):
    return pi*d/180.0

def radian2Deg(r):
    return 360.0 * r/(2.0*pi)

def rX(v, alpha, t):
    return v*cos(deg2Radian(alpha))*t

def rY(v, alpha, t):
    return v*sin(deg2Radian(alpha))*t - g*t*t/2.0

g = 9.8
v0 = 400.0
rmax = 16000.0
#rmax = v0**2 * sin(2*beta)/g
#sin(2*beta) = rmax*g/v0**2
#在一二象限有sin(a) = sin(pi - a)
beta = arcsin(rmax*g/v0**2)/2.0
gamma = (pi - arcsin(rmax*g/v0**2))/2.0

print 'v0:%f, beta:%f, gamma:%f' % (v0, radian2Deg(beta), radian2Deg(gamma))

