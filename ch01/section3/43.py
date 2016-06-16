#(a)通过画函数f(x) = sqrt(x**2 + x + 1) - x 的图形来估算lim(x->∞)f(x)
# 0.5
#
#(b)通过f(x)的一个列表来估计(a)中的极限值, 证明猜测
# 0.5
# 证明办法, (sqrt(x**2 + x + 1) - x) * (sqrt(x**2 + x + 1) + x) / (sqrt(x**2 + x + 1) + x)
# = (x**2 + x + 1 - x**2) / (sqrt(x**2 + x + 1) + x)
# = (x + 1) / (sqrt(x**2 + x + 1) + x)
# = (1 + 1/x) / sqrt(1 + 1/x + 1/x**2) + 1
#lim(x->∞)(1 + 1/x) / sqrt(1 + 1/x + 1/x**2) + 1
# = 1/2

def f(x):
    return sqrt(x**2 + x + 1) - x

x = linspace(0, 100, 100)
y = f(x)

print y

xlabel('x')
ylabel('y')
plot(x, y, 'r-')
