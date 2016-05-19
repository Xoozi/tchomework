
#求参数方程：
#抛物线x-1 = y**2的下半部分
#x(t) = t
#y(t) = -sqrt(t-1)
# 1<=t<=+∞

def f(t):
    return t

def g(t):
    return -sqrt(t-1)

t = linspace(1, 10, 100)

x = f(t)
y = g(t)


xlabel('x')
ylabel('y')
plot(x, y, 'r-');
