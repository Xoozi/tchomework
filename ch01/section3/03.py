
#求函数x->∞ 和 x->-∞ 时的极限
#lim(x->∞)(-5 + 7/x)/(3 - 1/x**2) = lim(x->∞)(-5 + 7/x) / lim(x->∞)(3 - 1/x**2) = -5 / 3

def f(x):
    return (-5 + 7/x)/(3 - 1/x**2)

x = linspace(-1000, 1000, 1000)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
