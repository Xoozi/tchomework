#5-8中, r(t)是在平面上运动的质点在时刻t的位置, 求在给定的时间区间内, 速度和加速度向量正交的一个或几个时刻
#7. r(t) = (3 cos t)i + (4 sin t)j, t >= 0

def rx(t):
    return 3*cos(t)

def ry(t):
    return 4*sin(t)

t = linspace(0, 2*pi, 1000)

x = rx(t)
y = ry(t)

plot(x, y, 'r-')

'''
v(t) = (-3 sin t)i + (4 cos t)j
a(t) = (-3 cos t)i + (-4 sin t)j

dot(v(t), a(t)) = 9 sin t cos t - 16 sin t cos t = 7 sin t cos t
故t = 2npi, t = 2npi + pi/2, t = 2npi + pi, t = 2npi + 3pi/2
时正交
'''
