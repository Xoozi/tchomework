
#求反函数
#f(x) = 50 / (1 + 1.1**(-x))
#解方程
# y = 50 / (1 + 1.1**(-x))
# 1 + 1.1**(-x) = 50 / y
# 1.1**(-x) = 50 / y - 1 = (50 - y) / y
# 1.1**x = y / (50 - y)
# x = log1.1(y/(50-y))
# x = ln(y/(50-y)/ln(1.1)

def f(x):
    return 50 / (1 + 1.1**(-x))

def g(x):
    return log(x/(50-x))/log(1.1)


x = linspace(0, 10, 100)
y = f(x)

x1 = linspace(f(10), f(0), 100)
y1 = g(x1)


xlabel('x')
ylabel('y')
plot(x, y, 'r-', x1, y1, 'g-')
