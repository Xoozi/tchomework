
#一个棒球被以20度角在高于地面3英尺处击打
#球刚好飞越Fenway球场的左墙, 这面墙高37英尺, 距本垒315英尺
#(a)球的初速率多少
#(b)球经过多久达到这面墙
#设发射位置在(0, 3.0)处
#位置向量函数为r = (x0 + (v0 cos(alpha))t)i + (y0 + (v0 sin(alpha))t - gt**2/2)j
#y分量公式 rY = y0 + (v0 sin(alpha))t - gt**2/2
#落地时rY = 37 = 3 + (v0 sin(alpha))t - gt**2/2
#rX = v0 cos(alpha) t = rmax
#t = rmax/(v0*cos(alpha))
#代入ry  =  y0 + (v0 sin(alpha))t - gt**2/2
#   ry = y0 + v0 sin(alpha) * rmax/(v0 cos alpha) - g*(rmax/(v0*cos(alpha))**2)/2
#   ry = y0 + rmax * tan(alpha) - g/2*rmax**2/(v0**2 * cos(alpha)**2)
#   g/2 * rmax**2/(v0**2 * cos(alpha)**2) = y0 + rmax * tan(alpha) - ry
#   g/2 * rmax**2/((y0 + rmax * tan(alpha) - ry)*cos(alpha)**2 = v0**2
#   v0 = sqrt(g/2 * rmax**2/((y0 + rmax * tan(alpha) - ry)*cos(alpha)**2))

def deg2Radian(d):
    return pi*d/180.0


def vfun(y0, ry,  rmax, alpha, g):
    return sqrt(g/2 * rmax**2/((y0 + rmax * tan(alpha) - ry)*cos(alpha)**2))



def rX(v, alpha, t):
    return v*cos(deg2Radian(alpha))*t

def rY(v, alpha, t):
    return v*sin(deg2Radian(alpha))*t - g*t*t/2.0


v0 = vfun(3.0, 37, 315, deg2Radian(20.0), 32.15)
t = 315/(v0 * cos(deg2Radian(20)))

print 'v0:%f, flying time:%f sec' % (v0, t)
