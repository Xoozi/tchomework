
#用参数做图法画出给定区间上方程的图形
#
#椭圆x = 4*cos(t), y = 2*sin(t)
#(a) 0 <= t <= 2*pi
#(b) 0 <= t <= pi
#(c) -pi/2 <= t < pi/2


def fx(t):
    return 4*cos(t)
def fy(t):
    return 2*sin(t)


t1 = linspace(0, 2*pi, 100)
t2 = linspace(0, pi, 100)

#xoozi有意思, 想不到第三幅图像是这样的
t3 = linspace(-pi/2, pi/2, 100)

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
title('0 <= t <= pi')

subplot(313)
plot(x3, y3, 'b-')
title('-pi/2 <= t <= pi/2')
