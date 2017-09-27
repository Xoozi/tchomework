
#一个高尔夫球以30度角和90英尺/秒的速度离开地面, 它将越过路线上水平距离135英尺
#处30英尺高的树顶部吗?


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

g = 32.15
v0 = 90.0
alpha = 30

#rx = v * cos(alpha) * t
#t = rx/(v * cos(alpha))
t135 = 135.0/(v0 * cos(deg2Radian(alpha)))
h135 = rY(v0, alpha, t135)

canPass = h135 > 30

print 't135:%f, h135:%f, canPass:%s' % (t135, h135, canPass)
