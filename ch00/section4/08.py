
# IPython log file
# 画出函数f(x) = 1 - 1 / x, x > 0的图形
# 并画上直线y = x， 利用对y = x 的对称性， 把f(x)的反函数 g(x)的图形画出来


def f(x):
    return 1 - 1 / x

x = linspace(0.1, 5, 100)
y = f(x)
x0 = array([0, 5])
y0 = array([0, 5])

xlabel('x')
ylabel('y')
plot(x, y, 'r-', x0, y0, 'g-', y, x, 'b--')
