
#拉近镜头来看可微性
#下列函数在x = 0可微吗?
#f(x) = |x| + 1,    g(x) = sqrt(x**2 + 0.0001) + 0.99
#f在x = 0不可微, 它的图形在x=0有一角, 而放大再多此角也不会变值

def f(x):
    return sqrt(x**2) + 0.5

def g(x):
    return sqrt(x**2 + 0.0001) + 0.99



x = linspace(-0.5, 0.5, 100000)
yf = f(x)
yg = g(x)

plot([-2, 2], [0, 0], '-k')
plot(x, yf, '-r', x, yg, '-g')

