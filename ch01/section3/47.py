
#画f(x)的图形, 解释曲线的公式和图形之间的关系
#首先, 在|x| >= 2 时f(x)无定义
#然后在 -2 < x < 2之间
#lim(x->-2)f(x) = -∞
#lim(x->2)f(x) = ∞
#在此之间, 有理函数次数为1, 斜渐进线为一条过原点的直线


def f(x):
    return x/sqrt(4 - x**2)

x1 = linspace(-10, -2.1, 100)
y1 = f(x1)
x2 = linspace(-1.9, 1.9, 100)
y2 = f(x2)
x3 = linspace(2.1, 10, 100)
y3 = f(x3)


xlabel('x')
ylabel('y')
plot(x1, y1, 'r-', x2, y2, 'g-', x3, y3, 'b-')
