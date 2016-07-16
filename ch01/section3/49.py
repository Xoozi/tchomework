
#画f(x)的图形, 解释曲线的公式和图形之间的关系
#首先, 在|x| >= 2 时f(x)无定义
#然后在 -2 < x < 2之间
#lim(x->-2)f(x) = -∞
#lim(x->2)f(x) = ∞
#在此之间, 有理函数次数为1, 斜渐进线为一条过原点的直线


def f(x):
    return x**(2.0/3.0) + x**(-1.0/3.0)
#xoozi 这类函数画不出来, 先放着

x = linspace(-100, 100, 100)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')