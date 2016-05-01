
# IPython log file
# 画出函数f(x) = x**1.5, x >= 0的图形
# 并画上直线y = x， 利用对y = x 的对称性， 把f(x)的反函数 g(x)的图形画出来


def f(x):
    return x**1.5

x = linspace(0, 5, 100)
y = f(x)
x0 = array([0, 5])
y0 = array([0, 5])

xlabel('x')
ylabel('y')
plot(x, y, 'r-', x0, y0, 'g-', y, x, 'b--')
