#把y = f(x) = 2*x**4 - 4*x**2 + 1及其一阶, 二阶导数的图形画在一起
#对f的性态和f', f''的正负号和值关系进行评注
#f'= 0 的根为 x = -1, x = 0, x = 1
#f''= 0 的根为x = -0.577, x = 0.577

#先由f'来观察   x < -1,             f' < 0  f递减
#               -1 < x < 0,         f' > 0  f递增
#               0 < x < 1,          f' < 0  f递减
#               x > 1,              f' > 0  f递增
#再看f''
#               x < -0.577,         f''> 0  f上凹
#               -0.577 < x < 0.577, f''< 0  f下凹
#               x > 0.577           f''> 0  f上凹

def f(x):
    return 2*x**4 - 4*x**2 + 1

def fd(x):
    return 8*x**3 - 8*x

def fdd(x):
    return 24*x**2 - 8

def ddd(s, e, a):

    plot([s, e], [0, 0], '-k')

    x = linspace(s, e, a)
    y = f(x)
    yd= fd(x)
    ydd=fdd(x)
    plot(x, y, '-r', x, yd, '-g', x, ydd, '-b')

ddd(-1.6, 1.6, 1000)
