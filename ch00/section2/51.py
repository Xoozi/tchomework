
# IPython log file
# 画函数f(x) = sqrt(x) 和 g(x) = sqrt(1-x)以及他们的(a)和 (b)积 (c)两个差 (d)两个商的图形

#对于f(x) = sqrt(x) 定义域是x>=0
#对于g(x) = sqrt(1-x) 定义域是x<=1
#所以对于两个函数的复合函数, 如果是和积差 定义域是0 <= x <= 1
#对于f(x)/g(x) 定义域是 0 <= x < 1
#对于g(x)/f(x) 定义域是 0 < x <= 1

def f(x):
    return sqrt(x)
def g(x):
    return sqrt(1-x)
def a(x):
    return f(x) + g(x)
def b(x):
    return f(x) * g(x)
def c_1(x):
    return f(x) - g(x)
def c_2(x):
    return g(x) - f(x)
def d_1(x):
    return f(x) / g(x)
def d_2(x):
    return g(x) / f(x)

x = linspace(0.00000001, 1-0.00000001, 100)
y1 = f(x)
y2 = g(x)
y3 = a(x)
y4 = b(x)
y5 = c_1(x)
y6 = c_2(x)
y7 = d_1(x)
y8 = d_2(x)
xlabel('x')
ylabel('y')

subplot(421)
plot(x, y1, 'r-')
title('f(x) = sqrt(x)')

subplot(422)
plot(x, y2, 'r-')
title('g(x) = sqrt(1-x)')

subplot(423)
plot(x, y3, 'r-')
title('a(x) = f(x) + g(x)')

subplot(424)
plot(x, y4, 'r-')
title('b(x) = f(x) * g(x)')

subplot(425)
plot(x, y5, 'r-')
title('c_1(x) = f(x) - g(x)')

subplot(426)
plot(x, y6, 'r-')
title('c_2(x) = g(x) - f(x)')

subplot(427)
plot(x, y7, 'r-')
title('d_1(x) = f(x) / g(x)')

subplot(428)
plot(x, y8, 'r-')
title('d_2(x) = g(x) / f(x)')
