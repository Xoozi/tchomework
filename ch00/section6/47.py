#一条更优美的曲线
#
#x = 3*cos(t) + cos(3*t), y = 3*sin(t) - sin(3*t),  0 <= t <= 2*pi


def fx1(t):
    return 3*cos(t) + cos(3*t)
def fy1(t):
    return 3*sin(t) - sin(3*t)
def fx2(t):
    return -3*cos(t) + cos(-3*t)
def fy2(t):
    return -3*sin(t) - sin(-3*t)


t = linspace(0, 2*pi, 100)


x1 = fx1(t)
y1 = fy1(t)

x2 = fx2(t)
y2 = fy2(t)



xlabel('x')
ylabel('y')

subplot(211)
plot(x1, y1, 'r-')
title('3')

subplot(212)
plot(x2, y2, 'g-')
title('-3')

