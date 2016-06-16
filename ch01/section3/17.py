#求函数f(x)的极限
#lim(x->∞)(x**(1/3) - x**(1/5))/(x**(1/3) + x**(1/5))
#=lim(x->∞)(1 - x**(-2/15))/(1 + x**(-2/15)) = 1/1 = 1
def f(x):
    return (pow(x, 1.0/3.0)  - pow(x, 1.0/5.0))/(pow(x, 1.0/3.0) + pow(x, 1.0/5.0))

x = linspace(-100, -1, 100)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
