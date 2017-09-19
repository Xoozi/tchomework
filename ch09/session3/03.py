
#3. r(t)是平面上运动的质点
#   r(t) = (sec t) i + (tan t)j, t = pi/6

def sec(t):
    return 1/cos(t)

def r3(t):
    return (sec(t), tan(t))

def r3x(t):
    return sec(t)

def r3y(t):
    return tan(t)

#(a)画质点路径的图形
t = linspace(0, pi/3, 1000)
x3 = r3x(t)
y3 = r3y(t)
plot(x3, y3, 'r-')


#(b)求t = pi/6的速度和加速度
def v3(t):
    return (sec(t)*tan(t), sec(t)*sec(t))

def a3(t):
    return (sec(t)*tan(t)*tan(t) + sec(t)*sec(t)*sec(t), sec(t)*tan(t)*sec(t)*2)
v = v3(pi/6)
a = a3(pi/6)

print 'When t = pi/2, v:(%f, %f), a:(%f, %f)' % (v[0], v[1], a[0], a[1])

#(c)求质点在给定时刻t运动的速率和方向
vv = sqrt(v[0]*v[0] + v[1]*v[1])
vd = (v[0]/vv, v[1]/vv)
print '               vv:%f, vd:(%f, %f)' % (vv, vd[0], vd[1])

#(d)把质点的速度写成它的速率和方向的乘积
#v = vv * vd
