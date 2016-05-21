
#用参数做图法画出给定区间上方程的图形
#
#抛物线 x = 2*t+3 y = t**2-1,  -2 <= t <=2

def fx(t):
    return 2*t+3
def fy(t):
    return t**2-1


t = linspace(-2, 2, 100)

x = fx(t)
y = fy(t)

xlabel('x')
ylabel('y')
plot(x, y, 'r-')
