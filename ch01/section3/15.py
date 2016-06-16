#求函数f(x)的极限
#lim(x->∞)(2*sqrt(x) + x**-1)/(3*x - 7)
#=lim(x->∞)(2*x**0.5 + x**-1)/(3*x - 7)
#=lim(x->∞)(2*x**-0.5 + x**-2)/(3 - 7/x)
#=0/3 = 0
def f(x):
    return (2*sqrt(x) + x**(-1))/(3*x - 7)

x = linspace(0, 100, 100)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
