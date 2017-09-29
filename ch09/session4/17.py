
#推铅球
#运动员推一个8磅13盎司的铅球到73英尺10英寸远,
#假定以和水平线成40度的角在高于地面6.5英尺处投掷, 求铅球的初速率
#设发射位置在(0, 6.5)处
#位置向量函数为r = (x0 + (v0 cos(alpha))t)i + (y0 + (v0 sin(alpha))t - gt**2/2)j
#y分量公式 rY = y0 + (v0 sin(alpha))t - gt**2/2
#落地时rY = 0 = y0 + (v0 sin(alpha))t - gt**2/2
#此种情况下最大射程rX = v0 * cos(alpha) * t => t = rX/(v0 * cos(alpha))
#将t代入rY = y0 + v0*sin(alpha)*rx/(v0*cos (alpha) - g rX**2/2(v0*cos(alpha))**2
#rY = y0 + rx*tan(alpha) - g*rx**2/(2v0**2*cos(alpha)**2)
#g*rx**2/(2v0**2*cos(alpha)**2) = y0 + rx*tan(alpha) - ry
#g*rx**2/((2*cos(alpha)**2) * (y0 + rx*tan(alpha) - ry)) = v0**2
#v0 = sqrt(g*rx**2/((2*cos(alpha)**2) * (y0 + rx*tan(alpha) - ry)))

def deg2Radian(d):
    return pi*d/180.0

def rX(v, alpha, t):
    return v*cos(deg2Radian(alpha))*t

def rY(v, alpha, t):
    return v*sin(deg2Radian(alpha))*t - g*t*t/2.0

def vfun(rx, y0, ry, alpha, g):
    return sqrt(g*rx**2/((2*cos(alpha)**2) * (y0 + rx*tan(alpha) - ry)))

g = 32.15
alpha = 40.0
rx = 73.0 + 10.0/12.0
v0 = vfun(rx, 6.5, 0, deg2Radian(40.0), g)


print 'v0:%f' % (v0)
