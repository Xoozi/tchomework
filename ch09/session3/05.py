#5-8中, r(t)是在平面上运动的质点在时刻t的位置, 求在给定的时间区间内, 速度和加速度向量正交的一个或几个时刻
#5. r(t) = (t - sin t)i + (1 - cos t)j, 0 <= t <= 2pi

def rx(t):
    return t - sin(t)

def ry(t):
    return 1 - cos(t)

t = linspace(0, 2*pi, 1000)

x = rx(t)
y = ry(t)

plot(x, y, 'r-')

'''
v(t) = (1 - cos t)i + (sin t)j
a(t) = (sin t)i + (cot t)j

dot(v(t), a(t)) = sin t - sin t cost + sin t cos t = sin
故t = 0, t = pi, t = 2pi三个时刻速度向量和加速度向量正交
'''
