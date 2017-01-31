#把f(x) = (x - 3)**2 * e**x及其一阶导数的图像画到一起, 解释f的行为
#同f'的符号及其数值之间的关系

def f(x):
    return (x - 3.0)**2 * e**x

def fd(x):
    return (x**2 - 4.0*x - 3.0)*e**x

x = linspace(-5, 5, 10000)
y = f(x)
yd= fd(x)

plot(x, y, '-r', x, yd, '-g')
