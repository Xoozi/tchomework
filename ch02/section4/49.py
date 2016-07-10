#正切函数图形的斜率
#把y = tan(x)及其导数在(-pi/2, pi/2)上的图形画在一起
#正切函数的图形看似有一个最小斜率?最大斜率? 斜率总是为负吗?
#从图形上看, 有最小斜率, 总是为正

def sec(x):
    return 1/cos(x)

def f(x):
    return tan(x)

def fd(x):
    return sec(x)**2


def draw_f(s, e, style):

    x = linspace(s, e, 100)
    y = f(x)

    xlabel('x')
    ylabel('y')
    plot(x, y, style)

def draw_fd(s, e, style):

    x = linspace(s, e, 100)
    y = fd(x)

    xlabel('x')
    ylabel('y')
    plot(x, y, style)


s = -pi/2+0.1
e = pi/2-0.1

draw_f(s, e, 'r-')
draw_fd(s, e, 'g-')


