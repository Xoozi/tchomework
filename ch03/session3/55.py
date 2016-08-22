#y = f(x), f(1) = 0, 且f'(x) = x**-1, 对这种曲线的凹性有什么好说的
#f''(x) = -1*x**-2
#从表达式可以看出二阶导数恒为负, 可见这种曲线会一直下凹, 没有拐点
def fd(x):
    return 1.0/x

def fdd(x):
    return -1.0/(x**2)

def ddd(s, e, a):

    plot([s, e], [0, 0], '-k')

    x = linspace(s, e, a)
    yd= fd(x)
    ydd=fdd(x)
    plot(x, yd, '-g', x, ydd, '-b')

ddd(0.1, 6, 1000)
