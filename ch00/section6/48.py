
#用参数做图法画出给定区间上方程的图形
#
#旋轮线x = t - sin(t) y = 1-cos(t)
#(a) 0 <= t <= 2*pi
#(b) 0 <= t <= 4*pi
#(c) pi <= t < 3*pi


def fx(t):
    return t - sin(t)
def fy(t):
    return 1 - cos(t)


t1 = linspace(0, 2*pi, 100)
t2 = linspace(0, 4*pi, 100)
t3 = linspace(pi,3*pi, 100)

x1 = fx(t1)
y1 = fy(t1)

x2 = fx(t2)
y2 = fy(t2)

x3 = fx(t3)
y3 = fx(t3)


xlabel('x')
ylabel('y')
plot(x1, y1, 'r-', x2, y2, 'g-', x3, y3, 'b-')
xlabel('x')
ylabel('y')

subplot(311)
plot(x1, y1, 'r-')
title('0 <= t <= 2*pi')

subplot(312)
plot(x2, y2, 'g-')
title('0 <= t <= 4*pi')

subplot(313)
plot(x3, y3, 'b-')
title('pi<= t <= 3*pi')
