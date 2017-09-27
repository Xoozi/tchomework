
#一个弹簧枪以45度角在地面发射一个高尔夫球, 在10米远处落地


def deg2Radian(d):
    return pi*d/180.0

def radian2Deg(r):
    return 360.0 * r/(2.0*pi)

def rX(v, alpha, t):
    return v*cos(deg2Radian(alpha))*t

def rY(v, alpha, t):
    return v*sin(deg2Radian(alpha))*t - g*t*t/2.0

#(a)球的初速率是多少
#rMax = v0**2 * sin(2*alpha)/g
#=>v0 = sqrt(rMax*g/sin(2*alpha))
g = 9.8
alpha = 45.0
v0 = sqrt(10*g)

#(b)对于同样的初速率, 求两个发射角, 他们使射程为6米
#rMax = 6 = v0**2 * sin(2*beta)/g
#sin(2*beta) = 6*g/v0**2
#在一二象限有sin(a) = sin(pi - a)
beta = arcsin(6.0*g/v0**2)/2.0
gamma = (pi - arcsin(6.0*g/v0**2))/2.0

print 'v0:%f, beta:%f, gamma:%f' % (v0, radian2Deg(beta), radian2Deg(gamma))

