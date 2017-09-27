#一个运动员以与水平成45度的角从地面以上6.5英尺处以44英尺/秒
#的速度推一个6.5磅的铅球, 球在抛出多久后在离挡板内边多远处落地
#设发射位置在(0, 6.5)处
#位置向量函数为r = (x0 + (v0 cos(alpha))t)i + (y0 + (v0 sin(alpha))t - gt**2/2)j
#y分量公式 rY = y0 + (v0 sin(alpha))t - gt**2/2
#落地时rY = 0 = y0 + (v0 sin(alpha))t - gt**2/2


def deg2Radian(d):
    return pi*d/180.0

def rX(v, alpha, t):
    return v*cos(deg2Radian(alpha))*t

def rY(v, alpha, t):
    return v*sin(deg2Radian(alpha))*t - g*t*t/2.0

#xoozi算了半天没对, 后来想到这里加速度要用英制
g = 32.15
v0 = 44.0
alpha = 45.0
p1 = poly1d([-g/2.0, 44*sin(deg2Radian(alpha)), 6.5])
t = roots(p1)[0]


R = rX(v0, alpha, t)
print 'Range max:%f ft, flying time:%f sec' % (R, t)
