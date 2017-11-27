#旋轮线, 一个质点在xy平面上运动, 它在时刻t的位置是:
#   r(t) = (t - sin t)i + (1 - cos t)j
#(a)画出r(t)的图形

def fx(t):
    return t - sin(t)

def fy(t):
    return 1 - cos(t)

vt = linspace(0, 10*pi, 1000)
vx = fx(vt)
vy = fy(vt)

plot(vx, vy, '-r')


#(b)求|v|和|a|的最大值与最小值
#v(t) = (1 - cos t)i + (sin t)j
#a(t) = (sin t)i + (cos t)j

#|v(t)|² = (1 - cos t)² + sin²t = 1 - 2cos t + cos²t + sin²t = 2 - 2cos t
#   0 <= |v(t)|² <= 2    =>   0 <= |v(t)| <= sqrt(2)
#   xoozi 这里我哈了, 2 - 2cos t 最大可能应该是4
#|a(t)|² = sin²t + cos²t = 1
#   |a(t)| 恒为1
