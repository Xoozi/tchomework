#求函数x->∞ 和 x->-∞ 时的极限
#lim(x->∞)(PI - 2/x**2) = (lim(x->∞)PI) + (lim(x->∞) 2/x**2) = PI

def f(x):
    return pi - 2/x**2

x = linspace(-1000, 1000, 1000)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
