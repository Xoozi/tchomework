#飞行时间和高度
#一个抛射体以初速率500米/秒和仰角45度发射

g = 9.8

def deg2Radian(d):
    return pi*d/180.0

def tMax(v, alpha):
    return 2*v*sin(deg2Radian(alpha))/g

def rMax(v, alpha):
    return v*v*sin(deg2Radian(2.0*alpha))/g

def hMax(v, alpha):
    return (v*sin(deg2Radian(alpha)))**2/(2.0*g)

def rX(v, alpha, t):
    return v*cos(deg2Radian(alpha))*t

def rY(v, alpha, t):
    return v*sin(deg2Radian(alpha))*t - g*t*t/2.0

v0 = 500.0
alpha = 45.0


#(a)抛射体何时多远处落地
t = tMax(v0, alpha)
R = rMax(v0, alpha)
print 'Range max:%f km, flying time:%f sec' % (R/1000.0, t)

#(b)抛射体在水平方向飞行5千米时在空中高度是多少
t5km = 5000/(v0*cos(deg2Radian(alpha)))
h5km = rY(v0, alpha, t5km)
print 'Height is %fkm, when h distance is 5km' % (h5km/1000.0)

#(c)抛射体达到的最大高度是多少
height = hMax(v0, alpha)
print 'The max height is %fkm' % (height/1000.0)
