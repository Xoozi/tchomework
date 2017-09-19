
#1. r(t)是平面上运动的质点
#   r(t) = (2 cos t) i + (3 sin t)j, t = pi/2
def r1(t):
    return (2.0*cos(t), 3.0*sin(t))

def r1x(t):
    return 2.0*cos(t)

def r1y(t):
    return 3.0*sin(t)

#(a)画质点路径的图形
t = linspace(0, 2*pi, 1000)
x1 = r1x(t)
y1 = r1y(t)
plot(x1, y1, 'r-')


#(b)求t = pi/2的速度和加速度
def v1(t):
    return (2.0*-sin(t), 3.0*cos(t))

def a1(t):
    return (2.0*-cos(t), 3.0*-sin(t))
v = v1(pi/2)
a = a1(pi/2)

print 'When t = pi/2, v:(%f, %f), a:(%f, %f)' % (v[0], v[1], a[0], a[1])

#(c)求质点在给定时刻t运动的速率和方向
vv = sqrt(v[0]*v[0] + v[1]*v[1])
vd = (v[0]/vv, v[1]/vv)
print '               vv:%f, vd:(%f, %f)' % (vv, vd[0], vd[1])

#(d)把质点的速度写成它的速率和方向的乘积
#v = vv * vd
