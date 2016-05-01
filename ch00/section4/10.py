
# IPython log file
# 画出函数f(x) = sin(x), -PI/2 <= x <= PI/2的图形
# 并画上直线y = x， 利用对y = x 的对称性， 把f(x)的反函数 g(x)的图形画出来


def f(x):
    return sin(x)

x = linspace(-pi/2, pi/2, 100)
y = f(x)
x0 = array([0, 5])
y0 = array([0, 5])

xlabel('x')
ylabel('y')
plot(x, y, 'r-', x0, y0, 'g-', y, x, 'b--')
