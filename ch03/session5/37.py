#无摩擦的小车
#从静止的位置把通过一个弹簧与墙相连的小车拉出10厘米
#然后在t = 0时刻松开, 让小车来回滚动4秒钟, 小车在t 时刻的位置为 s(t) = 10*cos(pi*t)
#(a)小车的最大速度是多少?何时小车运动有这么快, 在什么位置, 加速度大小为多少
#(b)当加速度达到最大时,小车位置在哪? 小车的速率为多少

#画好图后, 都不想答这题了

def s(t):
    return 10*cos(pi*t)

def v(t):
    return -10*pi*sin(pi*t)

def a(t):
    return -10*pi**2*cos(pi*t)

plot([0, 4], [0, 0], '-k')

x = linspace(0, 4, 1000)
ys = s(x)
yv = v(x)
ya = a(x)

plot(x, ys, '-r', x, yv, '-g', x, ya, '-b')


