#r(t)是在平面上运动的质点在时刻t的位置, 求在给定的t的值, 速度和加速度向量的夹角
#9. r(t) = (2 cos t)i + (sin t)j, t = pi/4

def dot(v, u):
    return v[0]*u[0] + v[1]*u[1]

def norm(v):
    return sqrt(dot(v, v))

def angle(v, u):
    return arccos(dot(v, u)/(norm(v)*norm(u)))

def radian2Deg(r):
    return 360.0 * r/(2.0*pi)

def v(t):
    return (-2.0*sin(t), cos(t))

def a(t):
    return (-2.0*cos(t), -sin(t))

v9 = v(pi/4.0)
a9 = a(pi/4.0)

angle9 = angle(v9, a9)

print 'angle radian:%f, degree:%f' % (angle9, radian2Deg(angle9))
